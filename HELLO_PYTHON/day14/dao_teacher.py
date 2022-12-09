import psycopg2

class DaoTeacher:
    def __init__(self):
        self.conn = psycopg2.connect(host='localhost', dbname='python',user='postgres',password='python',port=5432)
        self.cur = self.conn.cursor() #java의 statement
    
    def selects(self):
        mydict = []
        self.cur.execute("SELECT t_id,t_name,mobile,addr FROM teacher order by t_id desc") 
        rows = self.cur.fetchall()
        for r in rows:
            #print(i)
             mydict.append({'t_id':r[0],'t_name':r[1],'mobile':r[2],'addr':r[3]})
        return mydict
    
    def select(self,t_id):
        sql = f"""
                SELECT 
                    t_id,t_name,mobile,addr 
                FROM 
                    teacher
                WHERE 
                    t_id='{t_id}'
        """
        self.cur.execute(sql) 
        rows = self.cur.fetchall()
        r = rows[0]
        ret = {'t_id':r[0],'t_name':r[1],'mobile':r[2],'addr':r[3]}
        return ret
    
    def insert(self,t_name,mobile,addr):
        sql = f"""
                INSERT INTO teacher
                    ( t_id, t_name, mobile, addr ) 
                VALUES 
                    (nextval('t_seq'), '{t_name}', '{mobile}', '{addr}')
            """
        
        self.cur.execute(sql)
        self.conn.commit()
        return self.cur.rowcount
    
    def update(self,t_id,t_name,mobile,addr):
        sql = f""" 
            update teacher
            set 
                t_name='{t_name}',
                mobile='{addr}',
                addr='{addr}'
            where 
                t_id='{t_id}'
         """    
        self.cur.execute(sql)
        self.conn.commit()
        return self.cur.rowcount
    
    def delete(self,t_id):
        sql = f""" 
                delete from teacher 
                      where t_id='{t_id}'
            """
        self.cur.execute(sql)
        self.conn.commit()
        return self.cur.rowcount
            
    def __del__(self):
        self.cur.close()
        self.conn.close()
        
    
if __name__ == '__main__':
    dt = DaoTeacher()
    teacher = dt.select('2')
    print(teacher)