import pandas as pd

# kakao 파일 불러오기
kakao_pre = pd.read_csv('C:\pythonProject1\Weather_Recommand\data\kakao_data.csv')
# print(kakao_pre)

# 366개의 행, 71개의 열
# kakao_pre = kakao_pre.iloc[0:366, 0:71]
# pd.set_option('display.max_rows', 367)
# pd.set_option('display.max_columns', 71)
# print(kakao_pre)

# # 1. column명 전처리
kakao_pre_columns = kakao_pre.columns # column명 추출

# # 컬럼명에서 '.1'이 있는 경우, 키워드만 나올 수 있도록 '.1' 삭제
columns_split = kakao_pre_columns.str.split(".")
kakao_pre_columns = columns_split.str.get(0)
kakao_pre.columns = kakao_pre_columns # 데이터프레임에 전처리한 컬럼명 다시 넣기
# print(kakao_pre_columns)
# print(kakao_pre)

# 2. 기준 값인 롱패딩을 100으로 맞추기

'''
11월 전처리 입니다.
'''
month_11 = kakao_pre.iloc[0:30,:]
# print(month_11)
long_pd = month_11['롱패딩']
# print(long_pd)
# print(google_pre.columns)

i = 1
j = 6
for b in [4, 100, 100, 100, 62, 62, 55, 62, 62, 62, 20, 62, 62, 62, 20, 62, 62, 62]:
    result = kakao_pre.iloc[0:30, i:j].astype(int) / b * 100
    i+=5
    j+=5
    print(result)

'''
line 114 ~ 296은 각 달에 맞는 롱패딩이 100이 되는 행을 찾아서 위 방법과 동일한 방식으로 전처리를 진행했습니다.
12월 전처리 입니다.
'''
month_12 = kakao_pre.iloc[30:61,:]
# print(month_11)
long_pd_12 = month_12['롱패딩']
# print(long_pd)
# print(google_pre.columns)

i = 1
j = 6
for b in [6, 100, 100, 100, 100, 67, 60, 67, 67, 67, 22, 67, 67, 67, 22, 67, 67, 67]:
    result = kakao_pre.iloc[0:30, i:j].astype(int) / b * 100
    i+=5
    j+=5
    print(result)

'''
1월 전처리 입니다.
'''
month_1 = kakao_pre.iloc[61:92,:]
# print(month_11)
month_1 = month_1['롱패딩']
# print(long_pd)
# print(google_pre.columns)

i = 1
j = 6
for b in [12, 100, 100, 100, 100, 100, 90, 100, 100, 100, 33, 100, 100, 100, 33, 100, 100, 100]:
    result = kakao_pre.iloc[0:30, i:j].astype(int) / b * 100
    i+=5
    j+=5
    print(result)

'''
2월 전처리 입니다.
'''
month_2 = kakao_pre.iloc[92:120,:]
# print(month_11)
month_2 = month_2['롱패딩']
# print(long_pd)
# print(google_pre.columns)

i = 1
j = 6
for b in [3, 100, 93, 86, 25, 25, 22, 25, 25, 25, 8, 25, 25, 25, 8, 25, 25, 25]:
    result = kakao_pre.iloc[0:30, i:j].astype(int) / b * 100
    i+=5
    j+=5
    print(result)

'''
3월 전처리 입니다.
'''
month_3 = kakao_pre.iloc[120:151,:]
# print(month_11)
month_3 = month_3['롱패딩']
# print(long_pd)
# print(google_pre.columns)

i = 1
j = 6
for b in [2, 33, 21, 27, 8, 8, 7, 8, 8, 8, 3, 8, 8, 8, 3, 8, 8, 8]:
    result = kakao_pre.iloc[0:30, i:j].astype(int) / b * 100
    i+=5
    j+=5
    print(result)

'''
4월 전처리 입니다.
'''
month_4 = kakao_pre.iloc[151:181,:]
# print(month_11)
month_4 = month_4['롱패딩']
# print(long_pd)
# print(google_pre.columns)

i = 1
j = 6
for b in [4, 74, 100, 84, 26, 26, 23, 26, 26, 26, 8, 26, 26, 26, 8, 26, 26, 26]:
    result = kakao_pre.iloc[0:30, i:j].astype(int) / b * 100
    i+=5
    j+=5
    print(result)

'''
5월 전처리 입니다.
'''
month_5 = kakao_pre.iloc[181:212,:]
# print(month_11)
month_5 = month_5['롱패딩']
# print(long_pd)
# print(google_pre.columns)

i = 1
j = 6
for b in [2, 12, 50, 25, 8, 8, 8, 8, 8, 8, 3, 8, 8, 8, 3, 8, 8 ]:
    result = kakao_pre.iloc[0:30, i:j].astype(int) / b * 100
    i+=5
    j+=5
    print(result)

'''
6월 전처리 입니다.
'''
month_6 = kakao_pre.iloc[212:242,:]
# print(month_11)
month_6 = month_6['롱패딩']
# print(long_pd)
# print(google_pre.columns)

i = 1
j = 6
for b in [2, 21, 100, 25, 9, 9, 8, 9, 9, 9, 3, 9, 9, 9, 3, 9, 9, 9]:
    result = kakao_pre.iloc[0:30, i:j].astype(int) / b * 100
    i+=5
    j+=5
    print(result)

'''
7월 전처리 입니다.
'''
month_7 = kakao_pre.iloc[242:273,:]
# print(month_11)
month_7 = month_7['롱패딩']
# print(long_pd)
# print(google_pre.columns)

i = 1
j = 6
for b in [1, 33, 93, 35, 14, 11, 8, 16, 8, 24, 4, 24, 24, 24, 4, 24, 24, 24]:
    result = kakao_pre.iloc[0:30, i:j].astype(int) / b * 100
    i+=5
    j+=5
    print(result)

'''
8월 전처리 입니다.
'''
month_8 = kakao_pre.iloc[273:304,:]
# print(month_11)
month_8 = month_8['롱패딩']
# print(long_pd)
# print(google_pre.columns)

i = 1
j = 6
for b in [1, 29, 50, 27, 15, 11, 8, 17, 9, 25, 4, 25, 25, 25, 4, 25, 25, 25]:
    result = kakao_pre.iloc[0:30, i:j].astype(int) / b * 100
    i+=5
    j+=5
    print(result)

'''
9월 전처리 입니다.
'''
month_9 = kakao_pre.iloc[304:334,:]
# print(month_11)
month_9 = month_9['롱패딩']
# print(long_pd)
# print(google_pre.columns)

i = 1
j = 6
for b in [6, 53, 94, 88, 46, 35, 26, 53, 26, 78, 13, 78, 78, 78, 13, 78, 78, 78]:
    result = kakao_pre.iloc[0:30, i:j].astype(int) / b * 100
    i+=5
    j+=5
    print(result)

'''
10월 전처리 입니다.
'''
month_10 = kakao_pre.iloc[334:365,:]
# print(month_11)
month_10 = month_10['롱패딩']
# print(long_pd)
# print(google_pre.columns)

i = 1
j = 6
for b in [7, 100, 60, 94, 59, 46, 34, 68, 34, 100, 17, 100, 100, 100, 17, 100, 100, 100]:
    result = kakao_pre.iloc[0:30, i:j].astype(int) / b * 100
    i+=5
    j+=5
    print(result)