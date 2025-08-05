#!/usr/bin/env python 

import pandas as pd
import numpy as np

# replace "?" with np.nan
def replace_question_with_nan(df):
    return df.replace("?", np.nan)

# convert columns to numeric
def convert_to_numeric(df):
    for col in df.columns:
        df[col] = pd.to_numeric(df[col])
    return df
