import psycopg2
#tweak the database parameters to match your specific postgres database.
conn = psycopg2.connect(host="localhost", 
                        port="5432", 
                        user="postgres", 
                        password="xuyuqing123456!", 
                        database="postgres"
                        #You may add the following line if you have schemaa
                        #,options="-c search_path=nfl"
                        )
cur = conn.cursor()
cur.execute("select * from employee limit 10")


conn.commit()
cur.close()
conn.close()