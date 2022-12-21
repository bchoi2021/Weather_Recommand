import pandas as pd

# 각 지역별 파일 읽기
chungju = pd.read_csv('C:\pythonProject1\Weather_Recommand\data\충청북도_충주_기온.csv')
boeun = pd.read_csv('C:\pythonProject1\Weather_Recommand\data\충청북도_보은_기온.csv')
hongseong = pd.read_csv('C:\pythonProject1\Weather_Recommand\data\충청남도_홍성_기온.csv')
jeju = pd.read_csv('C:\pythonProject1\Weather_Recommand\data\제주도_제주_기온.csv')
jangsu = pd.read_csv('C:\pythonProject1\Weather_Recommand\data\전라북도_장수_기온.csv')
Yeonggwang = pd.read_csv('C:\pythonProject1\Weather_Recommand\data\전라남도_영광군_기온.csv')
seoul = pd.read_csv('C:\pythonProject1\Weather_Recommand\data\서울특별시_서울_기온.csv')
Uiseong = pd.read_csv('C:\pythonProject1\Weather_Recommand\data\경상북도_의성_기온.csv')
Uiryeong = pd.read_csv('C:\pythonProject1\Weather_Recommand\data\경상남도_의령군_기온.csv')
paju = pd.read_csv('C:\pythonProject1\Weather_Recommand\data\경기도_파주_기온.csv')

# 불필요한 '지점' 컬럼 삭제
chungju_pre = chungju.drop(['지점'], axis = 'columns')
# print(chungju_pre)

boeun_pre = boeun.drop(['지점'], axis = 'columns')
# print(boeun_pre)

hongseong_pre = hongseong.drop(['지점'], axis = 'columns')
# print(hongseong_pre)

jeju_pre = jeju.drop(['지점'], axis = 'columns')
# print(jeju_pre)

jangsu_pre = jangsu.drop(['지점'], axis = 'columns')
# print(jangsu_pre)

Yeonggwang_pre = Yeonggwang.drop(['지점'], axis = 'columns')
# print(Yeonggwang_pre)

seoul_pre = seoul.drop(['지점'], axis = 'columns')
# print(seoul_pre)

Uiseong_pre = Uiseong.drop(['지점'], axis = 'columns')
# print(Uiseong_pre)

paju_pre = paju.drop(['지점'], axis = 'columns')
# print(paju_pre)