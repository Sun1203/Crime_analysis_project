import logging
import cx_Oracle
import json
from dto import *


class InfoDAO:

    # 회원가입
    def insertjoin(self, dto):
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
        cur = conn.cursor()

        try:
            cur.execute("insert into userjoin values (:userid, :userpw, :username)", userid=dto.getUserid(), userpw=dto.getUserpw(), username=dto.getUsername())
            # print("--------test")
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            cur.close()
            conn.close()



    def login(self, dto):
        data = ''
        try:
            conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur = conn.cursor()
            try:
                cur.execute("select userpw, userid from userjoin where nid=:nid, npw=:npw", nid=dto.getNid(), npw = dto.getNpw()) 
                row = cur.fetchone()
                print(row, "_______1")
                data = '{"userpw":"' + row[0] + '"}'
                
                print(data,"___________2")
                
            except Exception as e:
                print(e) 

        except Exception as e:
            print(e) 

        finally:
            cur.close() 
            conn.close()

        return data

    


if __name__ == "__main__":
    a = InfoDAO()
    # b = userjoindto("absasa", "124141", "abcc2121")
    # a.insertjoin(b)
    b = logindto('이재선짱짱맨', '12')
    a.login(b)