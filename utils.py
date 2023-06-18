"""
Date 2023-06-16
"""




def get_gt_modifiers():
    """
    Get the GT Positive and Negative Modifiers

    See paper GT(2021), Monetary Policy Press Releases: An International Comparison
    """
    modifiers = {}

    for txt in ["positive", "negative"]:
        with open(f"data/{txt}.txt", 'r') as f:
            p        = f.read()
            ans      = str(p).replace('\n','').split(",")
            arr      = [a.lstrip() for a in ans]
            modifiers[txt] = arr 

    return modifiers 