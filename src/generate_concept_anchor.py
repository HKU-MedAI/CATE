import os
import torch
from conch.open_clip_custom import create_model_from_pretrained, tokenize, get_tokenizer
from prompts import brca_prompts, nsclc_prompts, rcc_prompts

save_path = "./prompt_feats/"
if not os.path.exists(save_path):
    os.makedirs(save_path)

conch_model, _ = create_model_from_pretrained('conch_ViT-B-16', checkpoint_path="./conch.bin")
conch_model.eval()
tokenizer = get_tokenizer()
cls_templates = brca_prompts()

feats = []
for i in range(len(cls_templates)):
            tokenized_templates = tokenize(texts=cls_templates[i], tokenizer=tokenizer)
            feats.append(conch_model.encode_text(tokenized_templates).detach())


# save feats
torch.save(feats, os.path.join(save_path, "brca_concepts.pt"))
