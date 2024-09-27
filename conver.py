import sqlite3
import pandas as pd

# SQLite 데이터베이스에 연결
# conn = sqlite3.connect('blog.db')

# # SQL 쿼리를 사용하여 데이터 가져오기
# query = "SELECT * FROM visited_book"  # 'posts' 테이블을 feather 파일로 변환한다고 가정합니다. 필요에 따라 테이블 이름을 변경하세요.
# df = pd.read_sql_query(query, conn, dtype={'book_id':str})

# # 연결 닫기
# conn.close()

# # Feather 파일로 데이터 저장
# df.to_feather('blog.feather')

df = pd.read_feather('blog.feather')
# df = df.set_index('id')
# df.to_feather('blog.feather')
print(df)

# import sqlite3

# # SQLite 데이터베이스에 연결
# conn = sqlite3.connect('blog.db')

# # 커서 생성
# cursor = conn.cursor()

# # 마지막 레코드 조회
# cursor.execute("SELECT * FROM visited_book ORDER BY id DESC LIMIT 1")
# last_record = cursor.fetchone()

# # 연결 닫기
# conn.close()

# # 결과 출력
# print(last_record)