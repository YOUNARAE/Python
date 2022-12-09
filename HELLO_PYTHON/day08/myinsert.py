import psycopg2

conn = psycopg2.connect(host='localhost', dbname='python',user='postgres',password='python',port=5432)
cur = conn.cursor() 

#"""는 쿼리를 통째로 넣을 수 있게 해준다
sql = """ 
    INSERT INTO sample 
        ( col01, col02, col03 ) 
    VALUES 
        ( 4, 3, 3 )
"""


cur.execute(sql) 
print("cnt",cur.rowcount)
conn.commit()

cur.close()
conn.close()
