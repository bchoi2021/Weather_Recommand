import pandas as pd
import numpy as np

# kakao 파일 불러오기
kakao_pre = pd.read_csv('C:\pythonProject1\Weather_Recommand\data\kakao.csv' )
print(kakao_pre)
exit()

# 366개의 행, 71개의 열
# google_pre = google_pre.iloc[0:366, 0:71]
# pd.set_option('display.max_rows', 367)
# pd.set_option('display.max_columns', 71)
# print(google_pre)

# # 1. column명 전처리
# kakao_pre_columns = kakao_pre.columns # column명 추출
#
# # 컬럼명에서 ':(대한민국)'이 있는 경우, 키워드만 나올 수 있도록 ':(대한민국)' 삭제
# columns_split = kakao_pre_columns.str.split(":")
# google_pre_columns = columns_split.str.get(0)
# kakao_pre.columns = google_pre_columns # 데이터프레임에 전처리한 컬럼명 다시 넣기

# date = google_pre['일']
# month = date.str.split("-")[0][0]

# 2. 기준 값인 롱패딩을 100으로 맞추기
month_11 = kakao_pre.iloc[0:30,:]
# print(month_11)
long_pd = month_11['롱패딩']
print(long_pd)

# month_11 = month_11.iloc[:,2:].astype('int')
# # print(month_11)
# month_11 = pd.to_numeric(month_11['롱패딩'])
# print(month_11)
# long_pd = month_11.index[month_11['롱패딩'] == 100]
# print(long_pd)
# bool_month11 = month_11['롱패딩'] == 100

# 롱패딩의 값이 처음으로 100이 나올 때의 인덱스 값이 19임. 따라서, 19행에 있는 모든 롱패딩의 값을 100으로 맞추고, 각 열에 해당하는 가중치를 곱함
# print(long_pd.iloc[19,2])
