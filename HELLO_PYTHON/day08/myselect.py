import psycopg2

conn = psycopg2.connect(host='localhost', dbname='python',user='postgres',password='python',port=5432)

cur = conn.cursor() #java의 statement
sql = f""" 
    SELECT col01,col02,col03
      FROM sample 
    """
cur.execute(sql) 
rows = cur.fetchall() #하나씩 가져오지 않고 여러개

print(rows)
for i in rows:
    print(i)

cur.close()
conn.close()
#from sympy.polys.polyconfig import query

# class Databases():
#     def __init__(self):
#         self.db = psycopg2.connect(host='localhost', dbname='python',user='postgres',password='python',port=5432)
#         self.cursor = self.db.cursor()
#
#     def __del__(self):
#         self.db.close()
#         self.cursor.close()
#
#     def execute(self,query,args={}):
#         self.cursor.execute(query,args)
#         row = self.cursor.fetchall()
#         return row
#
#     def commit(self):
#         self.cursor.commit()
#
# if __name__ == "__main__":
#     query = "SELECT * FROM SAMPLE"
#     db = Databases()
#     print(db.execute(query))


#
# import psycopg2
#
# conn = psycopg2.connect(
#         host = "localhost",
#         port = 5432,
#         dbname = "python",
#         user="postgres",
#         password="python")
#
# cursor = conn.cursor()
# cursor.execute("SELECT * FROM SAMPLE") 
# data = cursor.fetchall()
# print(data) 


    
    