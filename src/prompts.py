def brca_prompts():
    prompts = [
        # Labels
        [
            'invasive ductal carcinoma',
            'breast invasive ductal carcinoma',
            'invasive ductal carcinoma of the breast',
            'invasive carcinoma of the breast, ductal pattern',
            'idc'
            ],
        [
            'invasive lobular carcinoma',
            'breast invasive lobular carcinoma',
            'invasive lobular carcinoma of the breast',
            'invasive carcinoma of the breast, lobular pattern',
            'ilc',
            ],
        # Adipocytes
        [
            'adipocytes',
            'adipose tissue',
            'fat cells',
            'fat tissue',
            'fat',
            ],
        # Connective tissue
        [
            'connective tissue',
            'stroma',
            'fibrous tissue',
            'collagen',
            ],
        # Necrotic Tissu
        [
            'necrotic tissue',
            'necrosis',
            ],
        # Normal Breast Tissue Cells
        [
            'normal breast tissue',
            'normal breast cells',
            'normal breast',
            ],
    ]

    templates = [
                "CLASSNAME.",
                "a photomicrograph showing CLASSNAME.",
                "a photomicrograph of CLASSNAME.",
                "an image of CLASSNAME.",
                "an image showing CLASSNAME.",
                "an example of CLASSNAME.",
                "CLASSNAME is shown.",
                "this is CLASSNAME.",
                "there is CLASSNAME.",
                "a histopathological image showing CLASSNAME.",
                "a histopathological image of CLASSNAME.",
                "a histopathological photograph of CLASSNAME.",
                "a histopathological photograph showing CLASSNAME.",
                "shows CLASSNAME.",
                "presence of CLASSNAME.",
                "CLASSNAME is present.",
                "an H&E stained image of CLASSNAME.",
                "an H&E stained image showing CLASSNAME.",
                "an H&E image showing CLASSNAME.",
                "an H&E image of CLASSNAME.",
                "CLASSNAME, H&E stain.",
                "CLASSNAME, H&E."
            ]

    cls_templates = []
    for i in range(len(prompts)):
        cls_template = []
        for j in range(len(prompts[i])):
            cls_template.extend([template.replace('CLASSNAME', prompts[i][j]) for template in templates])
        cls_templates.append(cls_template)
    return cls_templates

def nsclc_prompts():
    prompts = [
        # Labels
        [
            'adenocarcinoma',
            'lung adenocarcinoma',
            'adenocarcinoma of the lung',
            'luad',
            ],
        [
            'squamous cell carcinoma',
            'lung squamous cell carcinoma',
            'squamous cell carcinoma of the lung',
            'lusc',
            ],

        # Connective tissue
        [
            'connective tissue',
            'stroma',
            'fibrous tissue',
            'collagen',
            ],
        # Necrotic Tissu
        [
            'necrotic tissue',
            'necrosis',
            ],
        # Normal Breast Tissue Cells
        [
            'normal lung tissue',
            'normal lung cells',
            'normal lung',
            ],
    ]

    templates = [
                "CLASSNAME.",
                "a photomicrograph showing CLASSNAME.",
                "a photomicrograph of CLASSNAME.",
                "an image of CLASSNAME.",
                "an image showing CLASSNAME.",
                "an example of CLASSNAME.",
                "CLASSNAME is shown.",
                "this is CLASSNAME.",
                "there is CLASSNAME.",
                "a histopathological image showing CLASSNAME.",
                "a histopathological image of CLASSNAME.",
                "a histopathological photograph of CLASSNAME.",
                "a histopathological photograph showing CLASSNAME.",
                "shows CLASSNAME.",
                "presence of CLASSNAME.",
                "CLASSNAME is present.",
                "an H&E stained image of CLASSNAME.",
                "an H&E stained image showing CLASSNAME.",
                "an H&E image showing CLASSNAME.",
                "an H&E image of CLASSNAME.",
                "CLASSNAME, H&E stain.",
                "CLASSNAME, H&E."
            ]

    cls_templates = []
    for i in range(len(prompts)):
        cls_template = []
        for j in range(len(prompts[i])):
            cls_template.extend([template.replace('CLASSNAME', prompts[i][j]) for template in templates])
        cls_templates.append(cls_template)
    return cls_templates


def rcc_prompts():
    prompts = [
        [
            'clear cell renal cell carcinoma',
            'renal cell carcinoma, clear cell type',
            'renal cell carcinoma of the clear cell type',
            'clear cell rcc'
        ],
        [
            'papillary renal cell carcinoma',
            'renal cell carcinoma, papillary type',
            'renal cell carcinoma of the papillary type',
            'papillary rcc'
        ],
        [
            'chromophobe renal cell carcinoma',
            'renal cell carcinoma, chromophobe type',
            'renal cell carcinoma of the chromophobe type',
            'chromophobe rcc'
        ],
        # Adipocytes
        [
            'adipocytes',
            'adipose tissue',
            'fat cells',
            'fat tissue',
            'fat',
            ],
        # Connective tissue
        [
            'connective tissue',
            'stroma',
            'fibrous tissue',
            'collagen',
            ],
        [
            'necrotic tissue',
            'necrosis',
            ],
        # Normal Breast Tissue Cells
        [
            'normal kidney tissue',
            'normal kidney cells',
            'normal kidney',
            ],
            ]

    templates = [
                "CLASSNAME.",
                "a photomicrograph showing CLASSNAME.",
                "a photomicrograph of CLASSNAME.",
                "an image of CLASSNAME.",
                "an image showing CLASSNAME.",
                "an example of CLASSNAME.",
                "CLASSNAME is shown.",
                "this is CLASSNAME.",
                "there is CLASSNAME.",
                "a histopathological image showing CLASSNAME.",
                "a histopathological image of CLASSNAME.",
                "a histopathological photograph of CLASSNAME.",
                "a histopathological photograph showing CLASSNAME.",
                "shows CLASSNAME.",
                "presence of CLASSNAME.",
                "CLASSNAME is present.",
                "an H&E stained image of CLASSNAME.",
                "an H&E stained image showing CLASSNAME.",
                "an H&E image showing CLASSNAME.",
                "an H&E image of CLASSNAME.",
                "CLASSNAME, H&E stain.",
                "CLASSNAME, H&E."
            ]

    cls_templates = []
    for i in range(len(prompts)):
        cls_template = []
        for j in range(len(prompts[i])):
            cls_template.extend([template.replace('CLASSNAME', prompts[i][j]) for template in templates])
        cls_templates.append(cls_template)
    return cls_templates