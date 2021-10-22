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
cur.execute("INSERT INTO employee (SELECT generate_series(1,500) AS id, substr(MD5(random()::text),0,10) AS fname, substr(MD5(random()::text),0,10) AS lname)")


conn.commit()
cur.close()
conn.close()