import pandas as pd

def adding_word_length(x):
    if pd.isna(x['CURRENT_FIX_INTEREST_AREA_LABEL']):
        return 0
    else:
        return len(x.CURRENT_FIX_INTEREST_AREA_LABEL)