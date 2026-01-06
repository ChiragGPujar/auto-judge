import pandas as pd
import re

def text_features(X):
    """
    Extract handcrafted numerical features from raw text.
    This function is used during both training and inference.
    """
    s = pd.Series(X)

    return pd.DataFrame({
        "text_len": s.apply(len),
        "num_digits": s.apply(lambda x: sum(c.isdigit() for c in x)),
        "num_symbols": s.apply(lambda x: len(re.findall(r"[+\-*/=<>^]", x))),
        "contains_graph": s.str.contains("graph", case=False).astype(int),
        "contains_dp": s.str.contains("dp|dynamic", case=False).astype(int),
        "contains_math": s.str.contains("math|number|prime", case=False).astype(int),
        "contains_recursion": s.str.contains("recursion|recursive", case=False).astype(int),
    })
