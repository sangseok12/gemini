import pandas as pd

# 파일 경로
file_path = 'Cooking.csv'

# 다른 인코딩 옵션을 사용하여 파일을 불러오기
try:
    CK = pd.read_csv(file_path, encoding='utf-8')
except UnicodeDecodeError:
    CK = pd.read_csv(file_path, encoding='euc-kr')

# 각 행의 'INQ_CNT', 'RCMM_CNT', 'SRAP_CNT' 값을 더한 후, 평균을 계산하여 'NEW_COL' 열로 추가
CK['NEW_COL'] = CK[['INQ_CNT', 'RCMM_CNT', 'SRAP_CNT']].sum(axis=1) / 3

#선택
selected_CK = CK.iloc[:, [2, 13]]

# 결측치가 있는 행 제거
CK_cl = selected_CK.dropna()