import pandas as pd
from pymongo import MongoClient

# CSV 파일 읽기
df = pd.read_csv('./gangnamApartment.csv', encoding='utf-8')
df2 = pd.read_csv('./gangnamOfficetel.csv', encoding='utf-8')

# MongoDB 클라이언트 설정
username = 'rootuser'  # 실제 MongoDB 사용자 이름
password = 'rootuser'  # 실제 MongoDB 사용자 비밀번호
url = '223.130.135.82:27017/'
client = MongoClient(f'mongodb://{username}:{password}@{url}')
db = client['mongo_db']  # 데이터베이스 이름 설정
apartments_lands = db['apartments']  # 컬렉션 이름 설정
officetels_lands = db['officetels']  # 컬렉션 이름 설정

# 기존 컬렉션의 데이터 삭제
# apartments_lands.delete_many({})
# officetels_lands.delete_many({})


# Apartment 데이터 삽입
lands_data = df.to_dict(orient='records')
apartments_lands.insert_many(lands_data)


# # Officetel 데이터 삽입
lands_data = df2.to_dict(orient='records')
officetels_lands.insert_many(lands_data)


print("Data inserted successfully into MongoDB")