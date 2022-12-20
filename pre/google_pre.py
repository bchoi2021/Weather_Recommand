import pandas as pd

# google trend data 파일 불러오기
google_pre = pd.read_csv('C:\pythonProject1\Weather_Recommand\data\google_data.csv')

# 366개의 행, 71개의 열인 것을 확인할 수 있음
# google_pre = google_pre.iloc[0:366, 0:71]
# pd.set_option('display.max_rows', 367)
# pd.set_option('display.max_columns', 71)
# print(google_pre)

# 1. column명 전처리
google_pre_columns = google_pre.columns # column명 추출

# 컬럼명에서 ':(대한민국)'이 있는 경우, 키워드만 나올 수 있도록 ':(대한민국)' 삭제
columns_split = google_pre_columns.str.split(":")
google_pre_columns = columns_split.str.get(0)
google_pre.columns = google_pre_columns # 데이터프레임에 전처리한 컬럼명 다시 넣기

# date = google_pre['일']
# month = date.str.split("-")[0][0]

# 2. 기준 값인 롱패딩을 100으로 맞추기

# 11월 전처리
month_11 = google_pre.iloc[0:30,:]
# print(month_11)
long_pd = month_11['롱패딩']
# print(long_pd)
# print(google_pre.columns)


'''롱패딩의 값이 처음으로 100이 나올 때의 인덱스 값이 19다.
따라서, 19행에 있는 모든 롱패딩의 값을 100으로 맞추고, 100으로 맞추기 위해 곱한 가중치를 각 열에 곱한다.
19번째 row에 롱패딩의 값이 100이 아닌 column은 1, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14번 column 이다.
'''

# # 1 column
# long_pd_first_column = long_pd.iloc[0:30,0:1]
# long_pd_first_column = long_pd_first_column / 4 * 100
# # print(long_pd_first_column.round(2))
# first_long_pd = google_pre.iloc[0:30,1:6]
# first_long_pd = first_long_pd.astype(int) / 4 *100
# print(first_long_pd)
#
#
# # 5, 6 column
# # print(long_pd.iloc[0:30,4:6])
# long_pd_sixth_column = long_pd.iloc[0:30,4:6]
# long_pd_sixth_column = long_pd_sixth_column.astype(int) / 62 * 100
# # print(long_pd_sixth_column.round(2))
# second_long_pd = google_pre.iloc[0:30,22:31]
# second_long_pd = second_long_pd / 62 *100
# # print(second_long_pd)
#
# # 7 column
# # print(long_pd.iloc[0:30,4:6])
# long_pd_seventh_column = long_pd.iloc[0:30,6:7]
# long_pd_seventh_column = long_pd_seventh_column.astype(int) / 55 * 100
# # print(long_pd_seventh_column.round(2))
# third_long_pd = google_pre.iloc[0:30,32:36]
# third_long_pd = third_long_pd / 55 *100
# print(third_long_pd)
#
# # 8,9,10 column
# # print(long_pd.iloc[0:30,4:6])
# long_pd_eighth_column = long_pd.iloc[0:30,7:10]
# long_pd_eighth_column = long_pd_eighth_column.astype(int) / 62 * 100
# # print(long_pd_eighth_column.round(2))
# fourth_long_pd = google_pre.iloc[0:30,37:51]
# fourth_long_pd = fourth_long_pd / 62 *100
# # print(fourth_long_pd)
#
# # 11 column
# # print(long_pd.iloc[0:30,4:6])
# long_pd_eleventh_column = long_pd.iloc[0:30,10:11]
# long_pd_eleventh_column = long_pd_eleventh_column.astype(int) / 20 * 100
# # print(long_pd_eleventh_column.round(2))
# fifth_long_pd = google_pre.iloc[0:30,52:56]
# fifth_long_pd = fifth_long_pd / 20 *100
# # print(fifth_long_pd)
#
# # 12, 13, 14 column
# # print(long_pd.iloc[0:30,4:6])
# long_pd_twelfth_column = long_pd.iloc[0:30,11:14]
# long_pd_twelfth_column = long_pd_twelfth_column.astype(int) / 62 * 100
# # print(long_pd_twelfth_column.round(2))
# sixth_long_pd = google_pre.iloc[0:30,57:71]
# sixth_long_pd = sixth_long_pd / 62 *100
# # print(sixth_long_pd)

'''
위 코드들이 너무 긴 것 같아, 몇 줄의 코드로 줄여보았습니다.
'''

i = 1
j = 6
for b in [4, 100, 100, 100, 62, 62, 55, 62, 62, 62, 20, 62, 62, 62]:
    result = google_pre.iloc[0:30, i:j].astype(int) / b * 100
    i+=5
    j+=5
    print(result)

# 12월 전처리
month_12 = google_pre.iloc[30:61,:]
long_pd_12 = month_12['롱패딩']
# print(long_pd)
# print(google_pre.columns)

# 롱패딩의 값이 처음으로 100이 나올 때의 인덱스 값이 19임
# 따라서, 19행에 있는 모든 롱패딩의 값을 100으로 맞추고, 100으로 맞추기 위해 곱한 가중치를 각 열에 곱함
# 19번째 row에 롱패딩의 값이 100이 아닌 column은 1, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14번 column 이다.

