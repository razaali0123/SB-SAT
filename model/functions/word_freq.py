import pandas as pd

def word_frequency(df):
    word_occ = df[['RECORDING_SESSION_LABEL','page_name' ,'CURRENT_FIX_INTEREST_AREA_ID','CURRENT_FIX_INTEREST_AREA_LABEL', 'word_length']].groupby(['RECORDING_SESSION_LABEL','page_name', 'CURRENT_FIX_INTEREST_AREA_ID' ,'CURRENT_FIX_INTEREST_AREA_LABEL'], as_index= False).count()
    word_occ.rename(columns = {"word_length":"word_occurance_count"}, inplace=True)
    df = df.merge(word_occ, on= ['RECORDING_SESSION_LABEL','page_name' ,'CURRENT_FIX_INTEREST_AREA_ID','CURRENT_FIX_INTEREST_AREA_LABEL'])
    return df