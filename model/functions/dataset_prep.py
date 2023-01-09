from tqdm import tqdm

def data_prep(df):
    subj = df.subj.unique()
    page_book = df.page_name.unique()
    matrix = []
    target = []
    subjects = []

    seq_len = 0

    for s in tqdm(subj):
        for pb in page_book:
            temp = df[(df.subj == s) & (df.page_name == pb)]
            if temp.shape[0] == 0:
                continue
            temp = temp.sort_values("CURRENT_FIX_INTEREST_AREA_ID")
            target.append(temp['acc'].iloc[0])
            temp = temp.drop(['RECORDING_SESSION_LABEL', 'book_name', 'page_name', 'CURRENT_FIX_INTEREST_AREA_LABEL', 'CURRENT_FIX_INTEREST_AREA_ID', \
                'subj', 'book', 'acc', 'language', 'sex'], axis = 1)
            if temp.shape[0] > seq_len:
                seq_len = temp.shape[0]
            matrix.append(temp.to_numpy())
            subjects.append(s)
    return matrix, target, subjects
    