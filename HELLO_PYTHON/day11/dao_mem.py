import psycopg2


class DaoMem:
    def __init__(self):
        self.conn = psycopg2.connect(host='localhost', dbname='python',user='postgres',password='python',port=5432)
        self.cur = self.conn.cursor() #java의 statement
    
    def selects(self):
        mydict = []
        self.cur.execute("SELECT m_id,m_nm,tel,ymd FROM member") 
        rows = self.cur.fetchall()
        for r in rows:
            #print(i)
             mydict.append({'m_id':r[0],'m_nm':r[1],'tel':r[2],'ymd':r[3]})
        return mydict
    
    def select(self,m_id):
        sql = f"""
                SELECT 
                    m_id,m_nm,tel,ymd 
                FROM 
                    member
                WHERE 
                    m_id='{m_id}'
        """
        self.cur.execute(sql) 
        rows = self.cur.fetchall()
        r = rows[0]
        ret = {'m_id':r[0],'m_nm':r[1],'tel':r[2],'ymd':r[3]}
        return ret
    
    def insert(self,m_id,m_nm,tel,ymd):
        sql = f"""
                INSERT INTO member
                    ( m_id, m_nm, tel, ymd ) 
                VALUES 
                    ('{m_id}', '{m_nm}', '{tel}', '{ymd}')
            """
        self.cur.execute(sql)
        self.conn.commit()
        return self.cur.rowcount

    def update(self,m_id,m_nm,tel,ymd):
        sql = f""" 
            update member
            set 
                m_nm='{m_nm}',
                tel='{tel}',
                ymd='{ymd}'
            where 
                m_id='{m_id}'
         """    
        self.cur.execute(sql)
        self.conn.commit()
        return self.cur.rowcount
    
    def delete(self,m_id):
        sql = f""" 
                delete from member 
                      where m_id='{m_id}'
            """
        self.cur.execute(sql)
        self.conn.commit()
        return self.cur.rowcount
        
if __name__ == '__main__':
    ds = DaoMem()
    cnt = ds.select(1)
    print(cnt)