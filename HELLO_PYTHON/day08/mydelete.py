import psycopg2


col01 = '4'
col02 = '8'
col03 = '8'

conn = psycopg2.connect(host='localhost', dbname='python',user='postgres',password='python',port=5432)
cur = conn.cursor() 

sql = f""" 
    update sample
    set 
        col02='{col02}',
        col03='{col03}'
    where 
        col01='{col01}'
"""

cur.execute(sql) 
print("cnt",cur.rowcount)
conn.commit()

cur.close()
conn.close()
