import psycopg2


col01 = '4'

conn = psycopg2.connect(host='localhost', dbname='python',user='postgres',password='python',port=5432)
cur = conn.cursor() 

sql = f""" 
    delete from sample 
          where col01='{col01}'
"""

cur.execute(sql) 
print("cnt",cur.rowcount)
conn.commit()

cur.close()
conn.close()
