import pandas as pd

# naver data lab 파일 불러오기
naver_pre = pd.read_csv('C:\pythonProject1\Weather_Recommand\data\\naver.csv')
naver_pre.rename(columns={'날짜':'일'}, inplace = 'True') # google.csv, kakao.csv 파일과 형식을 동일하게 하기 위해 '날짜'로 되어 있는 컬럼명을 '일'로 수정
print(naver_pre)