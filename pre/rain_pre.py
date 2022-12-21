import pandas as pd

# 각 지역별 파일 읽기
chungju = pd.read_csv('C:\pythonProject1\Weather_Recommand\data\충청북도_충주.csv')
boeun = pd.read_csv('C:\pythonProject1\Weather_Recommand\data\충청북도_보은.csv')
hongseong = pd.read_csv('C:\pythonProject1\Weather_Recommand\data\충청남도_홍성.csv')
jeju = pd.read_csv('C:\pythonProject1\Weather_Recommand\data\제주도_제주.csv')
jangsu = pd.read_csv('C:\pythonProject1\Weather_Recommand\data\전라북도_장수.csv')
Yeonggwang = pd.read_csv('C:\pythonProject1\Weather_Recommand\data\전라남도_영광군.csv')
seoul = pd.read_csv('C:\pythonProject1\Weather_Recommand\data\서울특별시_서울.csv')
Uiseong = pd.read_csv('C:\pythonProject1\Weather_Recommand\data\경상북도_의성.csv')
Uiryeong = pd.read_csv('C:\pythonProject1\Weather_Recommand\data\경상남도_의령군csv.csv')
paju = pd.read_csv('C:\pythonProject1\Weather_Recommand\data\경기도_파주.csv')

'''
널 값이 있으므로 널 값을 0으로 채운다. 널 값을 모두 실제 강수량 그래프와 비교하여 확인했을 때, 강수량이 0일 때 널 값으로 나타나는 것을 발견했음. 
충청북도 충주 전처리 입니다.
'''
# 불필요한 '지점' 컬럼 삭제
chungju_pre = chungju.drop(['지점'], axis = 'columns')
# print(chungju_pre)

# 널 값이 있는지 확인
# print(chungju_pre.isnull().sum())

chungju = chungju_pre.fillna(0)
# print(chungju)

'''
충청북도 보은 전처리 입니다.
'''
# 불필요한 '지점' 컬럼 삭제
boeun_pre = boeun.drop(['지점'], axis = 'columns')
# print(boeun_pre)

# 널 값이 있는지 확인
# print(boeun_pre.isnull().sum())

boeun = boeun_pre.fillna(0)
# print(boeun)

'''
충청남도 홍성 전처리 입니다.
'''
# 불필요한 '지점' 컬럼 삭제
hongseong_pre = hongseong.drop(['지점'], axis = 'columns')
# print(hongseong_pre)

# 널 값이 있는지 확인
# print(hongseong_pre.isnull().sum())

hongseong = hongseong_pre.fillna(0)
# print(hongseong)

'''
제주도 제주 전처리 입니다.
'''
# 불필요한 '지점' 컬럼 삭제
jeju_pre = jeju.drop(['지점'], axis = 'columns')
# print(jeju_pre)

# 널 값이 있는지 확인
# print(jeju_pre.isnull().sum())

jeju = jeju_pre.fillna(0)
# print(jeju)

'''
전라북도 장수 전처리 입니다.
'''
# 불필요한 '지점' 컬럼 삭제
jangsu_pre = jangsu.drop(['지점'], axis = 'columns')
# print(jangsu_pre)

# 널 값이 있는지 확인
# print(jangsu_pre.isnull().sum())

jangsu = jangsu_pre.fillna(0)
# print(jangsu)

'''
전라북도 영광군 전처리 입니다.
'''
# 불필요한 '지점' 컬럼 삭제
Yeonggwang_pre = Yeonggwang.drop(['지점'], axis = 'columns')
# print(Yeonggwang_pre)

# 널 값이 있는지 확인
# print(Yeonggwang_pre.isnull().sum())

Yeonggwang = Yeonggwang_pre.fillna(0)
# print(Yeonggwang)

'''
서울특별시 서울 전처리 입니다.
'''
# 불필요한 '지점' 컬럼 삭제
seoul_pre = seoul.drop(['지점'], axis = 'columns')
# print(seoul_pre)

# 널 값이 있는지 확인
# print(seoul_pre.isnull().sum())

seoul = seoul_pre.fillna(0)
# print(seoul)

'''
경상북도 의성 전처리 입니다.
'''
# 불필요한 '지점' 컬럼 삭제
Uiseong_pre = Uiseong.drop(['지점'], axis = 'columns')
# print(Uiseong_pre)

# 널 값이 있는지 확인
# print(Uiseong_pre.isnull().sum())

Uiseong = Uiseong_pre.fillna(0)
# print(Uiseong)

'''
경상남도 의령 전처리 입니다.
'''
# 불필요한 '지점' 컬럼 삭제
Uiryeong_pre = Uiryeong.drop(['지점'], axis = 'columns')
# print(Uiryeong_pre)

# 널 값이 있는지 확인
# print(Uiryeong_pre.isnull().sum())

Uiryeong = Uiryeong_pre.fillna(0)
# print(Uiryeong)

'''
경기도 파주 전처리 입니다.
'''
# 불필요한 '지점' 컬럼 삭제
paju_pre = paju.drop(['지점'], axis = 'columns')
# print(paju_pre)

# 널 값이 있는지 확인
# print(paju_pre.isnull().sum())

paju = paju_pre.fillna(0)
# print(paju)

'''
널 값을 채운 각 지역별 데이터를 합치겠습니다.(merge를 사용했습니다.)
'''
merged_df1 = pd.merge(chungju, boeun, on='날짜') # 충주, 보은 데이터 합침
merged_df2 = pd.merge(jeju, jangsu, on='날짜') # 제주, 장수 데이터 합침
merged_df3 = pd.merge(Yeonggwang, seoul, on='날짜') # 영광, 서울 데이터 합침
merged_df4 = pd.merge(Uiseong, Uiryeong, on='날짜') # 의성, 의령 데이터 합침
merged_df5 = pd.merge(hongseong, paju, on='날짜') # 홍성, 파주 데이터 합침
merged_df_1 = pd.merge(merged_df1, merged_df2, on='날짜') # 충주, 보은, 제주, 장수 데이터 합침
merged_df_2 = pd.merge(merged_df3, merged_df4, on='날짜') # 영광, 서울, 의성, 의령 데이터 합침
merged_data = pd.merge(merged_df_1, merged_df_2, on='날짜') # 충주, 보은, 제주, 장수, 영광, 서울, 의성, 의령 데이터 합침
merged_data2 = pd.merge(merged_data, merged_df5, on='날짜') # merged_data2에 홍성 데이터 합침

# merged_data2를 출력했을 때, 컬럼명이 X_Y 이런식으로 나오기 때문에 각 지역명으로 컬럼명을 변경함
merged_data2.columns = ['날짜','chungju','boeun','jeju','jansu','Yeonggwang','seoul','Uiseong','Uiryeong','hongseong','paju']
print(merged_data2)