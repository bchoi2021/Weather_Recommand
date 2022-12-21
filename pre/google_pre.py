import pandas as pd

# google trend data 파일 불러오기
google_pre = pd.read_csv('C:\pythonProject1\Weather_Recommand\data\google.csv')
print(google_pre)

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


'''
가중치를 곱하여 동일한 기준으로 만드는 과정은 다음과 같다. 먼저, 11월을 예시로 들어보겠습니다.
롱패딩의 값이 처음으로 100이 나올 때의 인덱스 값이 19다. 따라서, 19행에 있는 모든 롱패딩의 값을 100으로 맞추고, 100으로 맞추기 위해 곱한 가중치를 롱패딩을 제외한 나머지 상품에도 각 열에 곱한다.
19번째 row에서, 롱패딩의 값이 100이 아닌 column은 1, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14번 column 이다.
따라서, 롱패딩 19번째 행에 있는 각 원소들을 100으로 만들기 위해 해당 원소를 원소로 나누어 1로 만든 후 다시 100을 곱한다.

아래 코드들은 한 컬럼씩 전처리를 진행한 코드들이며, 이 코드들의 효율성을 위해 line 100 ~ 106에 규칙을 찾아서 간결화하여 나타냈습니다.
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
위 코드들이 너무 긴 것 같아, 몇 줄의 코드로 간결화해보았습니다.
위 코드들의 규칙을 살펴보니, 롱패딩 한 개를 기준으로 4개씩의 상품의 수치가 나타나고, 같은 달에서 롱패딩에 따른 열의 범위를 다르게 해주면 된다는 사실을 알 수 있습니다.
또한, 열의 범위는 5씩 증가하기 때문에 i와 j를 활용하여 for문을 작성했습니다.
'''

i = 1
j = 6
for b in [4, 100, 100, 100, 62, 62, 55, 62, 62, 62, 20, 62, 62, 62, 20, 62, 62, 62]:
    result = google_pre.iloc[0:30, i:j].astype(int) / b * 100
    i+=5
    j+=5
    print(result)

'''
line 114 ~ 296은 각 달에 맞는 롱패딩이 100이 되는 행을 찾아서 위 방법과 동일한 방식으로 전처리를 진행했습니다.
12월 전처리 입니다.
'''
month_12 = google_pre.iloc[30:61,:]
# print(month_11)
long_pd_12 = month_12['롱패딩']
# print(long_pd)
# print(google_pre.columns)

i = 1
j = 6
for b in [6, 100, 100, 100, 100, 67, 60, 67, 67, 67, 22, 67, 67, 67, 22, 67, 67, 67]:
    result = google_pre.iloc[0:30, i:j].astype(int) / b * 100
    i+=5
    j+=5
    print(result)

'''
1월 전처리 입니다.
'''
month_1 = google_pre.iloc[61:92,:]
# print(month_11)
month_1 = month_1['롱패딩']
# print(long_pd)
# print(google_pre.columns)

i = 1
j = 6
for b in [12, 100, 100, 100, 100, 100, 90, 100, 100, 100, 33, 100, 100, 100, 33, 100, 100, 100]:
    result = google_pre.iloc[0:30, i:j].astype(int) / b * 100
    i+=5
    j+=5
    print(result)

'''
2월 전처리 입니다.
'''
month_2 = google_pre.iloc[92:120,:]
# print(month_11)
month_2 = month_2['롱패딩']
# print(long_pd)
# print(google_pre.columns)

i = 1
j = 6
for b in [3, 100, 93, 86, 25, 25, 22, 25, 25, 25, 8, 25, 25, 25, 8, 25, 25, 25]:
    result = google_pre.iloc[0:30, i:j].astype(int) / b * 100
    i+=5
    j+=5
    print(result)

'''
3월 전처리 입니다.
'''
month_3 = google_pre.iloc[120:151,:]
# print(month_11)
month_3 = month_3['롱패딩']
# print(long_pd)
# print(google_pre.columns)

i = 1
j = 6
for b in [2, 33, 21, 27, 8, 8, 7, 8, 8, 8, 3, 8, 8, 8, 3, 8, 8, 8]:
    result = google_pre.iloc[0:30, i:j].astype(int) / b * 100
    i+=5
    j+=5
    print(result)

'''
4월 전처리 입니다.
'''
month_4 = google_pre.iloc[151:181,:]
# print(month_11)
month_4 = month_4['롱패딩']
# print(long_pd)
# print(google_pre.columns)

i = 1
j = 6
for b in [4, 74, 100, 84, 26, 26, 23, 26, 26, 26, 8, 26, 26, 26, 8, 26, 26, 26]:
    result = google_pre.iloc[0:30, i:j].astype(int) / b * 100
    i+=5
    j+=5
    print(result)

'''
5월 전처리 입니다.
'''
month_5 = google_pre.iloc[181:212,:]
# print(month_11)
month_5 = month_5['롱패딩']
# print(long_pd)
# print(google_pre.columns)

i = 1
j = 6
for b in [2, 12, 50, 25, 8, 8, 8, 8, 8, 8, 3, 8, 8, 8, 3, 8, 8 ]:
    result = google_pre.iloc[0:30, i:j].astype(int) / b * 100
    i+=5
    j+=5
    print(result)

'''
6월 전처리 입니다.
'''
month_6 = google_pre.iloc[212:242,:]
# print(month_11)
month_6 = month_6['롱패딩']
# print(long_pd)
# print(google_pre.columns)

i = 1
j = 6
for b in [2, 21, 100, 25, 9, 9, 8, 9, 9, 9, 3, 9, 9, 9, 3, 9, 9, 9]:
    result = google_pre.iloc[0:30, i:j].astype(int) / b * 100
    i+=5
    j+=5
    print(result)

'''
7월 전처리 입니다.
'''
month_7 = google_pre.iloc[242:273,:]
# print(month_11)
month_7 = month_7['롱패딩']
# print(long_pd)
# print(google_pre.columns)

i = 1
j = 6
for b in [1, 33, 93, 35, 14, 11, 8, 16, 8, 24, 4, 24, 24, 24, 4, 24, 24, 24]:
    result = google_pre.iloc[0:30, i:j].astype(int) / b * 100
    i+=5
    j+=5
    print(result)

'''
8월 전처리 입니다.
'''
month_8 = google_pre.iloc[273:304,:]
# print(month_11)
month_8 = month_8['롱패딩']
# print(long_pd)
# print(google_pre.columns)

i = 1
j = 6
for b in [1, 29, 50, 27, 15, 11, 8, 17, 9, 25, 4, 25, 25, 25, 4, 25, 25, 25]:
    result = google_pre.iloc[0:30, i:j].astype(int) / b * 100
    i+=5
    j+=5
    print(result)

'''
9월 전처리 입니다.
'''
month_9 = google_pre.iloc[304:334,:]
# print(month_11)
month_9 = month_9['롱패딩']
# print(long_pd)
# print(google_pre.columns)

i = 1
j = 6
for b in [6, 53, 94, 88, 46, 35, 26, 53, 26, 78, 13, 78, 78, 78, 13, 78, 78, 78]:
    result = google_pre.iloc[0:30, i:j].astype(int) / b * 100
    i+=5
    j+=5
    print(result)

'''
10월 전처리 입니다.
'''
month_10 = google_pre.iloc[334:365,:]
# print(month_11)
month_10 = month_10['롱패딩']
# print(long_pd)
# print(google_pre.columns)

i = 1
j = 6
for b in [7, 100, 60, 94, 59, 46, 34, 68, 34, 100, 17, 100, 100, 100, 17, 100, 100, 100]:
    result = google_pre.iloc[0:30, i:j].astype(int) / b * 100
    i+=5
    j+=5
    print(result)