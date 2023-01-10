from tqdm import tqdm
import numpy as np

def data_prep(df, seq_len = 200):
    subj = df.subj.unique()
    page_book = df.page_name.unique()
    a = len(page_book)
    z = len(subj) * a
    num_features = df.drop(['RECORDING_SESSION_LABEL', 'book_name', 'page_name', 'CURRENT_FIX_INTEREST_AREA_LABEL', 'CURRENT_FIX_INTEREST_AREA_ID', \
                'subj', 'book', 'acc', 'language', 'sex'], axis = 1).shape[1]

    matrix = np.zeros(shape = (z, seq_len, num_features))

    #matrix = []
    target = []
    mask = []


    for cnt_person, s in enumerate(tqdm(subj)):
        for cnt, pb in enumerate(page_book):
            temp = df[(df.subj == s) & (df.page_name == pb)]
            if temp.shape[0] == 0:
                mask.append(('na', 'na'))
                target.append('na')
                continue
            temp = temp.sort_values("CURRENT_FIX_INTEREST_AREA_ID")
            target.append(temp['acc'].iloc[0])
            temp = temp.drop(['RECORDING_SESSION_LABEL', 'book_name', 'page_name', 'CURRENT_FIX_INTEREST_AREA_LABEL', 'CURRENT_FIX_INTEREST_AREA_ID', \
                'subj', 'book', 'acc', 'language', 'sex'], axis = 1)
            if temp.shape[0] >= seq_len:

                temp = (temp.iloc[:seq_len, :]).to_numpy()
            else:
                diff = seq_len - temp.shape[0]
                to_add = np.zeros(shape= (diff, temp.shape[1]))

                temp = temp.to_numpy()

                temp = np.append(temp, to_add, axis=0)


            matrix[cnt_person*a + cnt, :, :] = temp
            mask.append((s,pb))
    return matrix, target, mask
    