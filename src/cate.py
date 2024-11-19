import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
from einops import rearrange, repeat
from infonce import InfoNCE

class CATE(nn.Module):
    def __init__(self, input_dim=512, ib_dim=512, interv_dim=512, concept_path="./prompt_feats/brca_concepts.pt"):
        super(CATE, self).__init__()

        self.feats = torch.load(concept_path)
        self.feats = [feat.to("cuda") for feat in self.feats]
        
        self.encoder_IB = nn.Sequential(
            nn.Linear(input_dim, ib_dim),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(ib_dim, ib_dim * 2),
        ).to("cuda")

        self.x_linear = nn.Sequential(
            nn.Linear(input_dim, ib_dim),
            nn.ReLU(),
        ).to("cuda")

        self.interv_linear = nn.Sequential(
            nn.Linear(self.feats[0].shape[0] + self.feats[1].shape[0], interv_dim),
            nn.ELU(),
            nn.AlphaDropout(p=0.4, inplace=False),
            ).to("cuda")

        self.infonce_loss = InfoNCE()

    def reparameterise(self, mu, logvar):
        epsilon = torch.randn_like(mu)
        return mu + epsilon * torch.exp(logvar / 2)

    def kl_loss(self, mu, logvar):
        kl_div = -0.5 * torch.mean(1 + logvar - mu.pow(2) - logvar.exp(), dim=-1)
        kl_mean = torch.mean(kl_div)
        return kl_mean
    def ib(self, x, label=None, results_dict=None):
        x_re = self.encoder_IB(x)
        mu, logvar = x_re.chunk(2, dim=-1)
        kl_loss = self.kl_loss(mu, logvar)
        results_dict['kl_loss'] = kl_loss
        x_re = self.reparameterise(mu, logvar)

        if label is not None:
            if label[0] == 0:
                sim = x @ self.feats[0].mean(dim=0)
                h_pos_0 = x_re[torch.topk(sim, 10)[1]]
                info_loss = self.infonce_loss(h_pos_0, repeat(self.feats[0].mean(dim=0), 'c -> b c', b=h_pos_0.shape[0]), torch.concat([torch.mean(self.feats[j], dim=0, keepdim=True) for j in range(len(self.feats)) if j != 0], dim=0))  # best
            elif label[0] == 1:
                sim = x @ self.feats[1].mean(dim=0)
                h_pos_1 = x_re[torch.topk(sim, 10)[1]]
                info_loss = self.infonce_loss(h_pos_1, repeat(self.feats[1].mean(dim=0), 'c -> b c', b=h_pos_1.shape[0]), torch.concat([torch.mean(self.feats[j], dim=0, keepdim=True) for j in range(len(self.feats)) if j != 1], dim=0))    # best
            
            results_dict[f'infonce_loss'] = info_loss

        x_c = (x_re @ torch.concat([self.feats[0], self.feats[1]]).T * 56.3477).detach()
        x_c = (x_c - x_c.mean(dim=(0, 1))) / x_c.std(dim=(0, 1))
        x_c = self.interv_linear(x_c)

        return x_re, x_c, results_dict
