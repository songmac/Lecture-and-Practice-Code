import pymysql

# Mysql처럼 connection 맺기

db = pymysql.connect(host='101.101.210.141', 
                     port=3306, 
                     user='study', # connection name
                     passwd='study!@#$%',   
                     db='ssy4748',  
                     charset='utf8')


# <TRY1>

# cursor = db.cursor()
# sql = """
#     CREATE TABLE ssy1 (
#     name nvarchar(20) NOT NULL, 
#     math INT NULL,
#     science INT NULL,
#     english INT NULL,
#     PRIMARY KEY (name)
#     )
# """

# cursor.execute(sql)
# db.commit() # mysql에서 autocommit 해제 되어있을 시 반드시 실행
# cursor.close()
# db.close()



# <TRY2>

# cursor = db.cursor()
# sql = """
#     INSERT INTO ssy1 (name, math, english)
#         VALUES('송수연', 80, 90)
# """

# cursor.execute(sql)
# db.commit()
# cursor.close()
# db.close()




# <TRY3>

# cursor = db.cursor()
# sql = """
#     UPDATE ssy1
#         SET math = 10,
#             english = 10
#     WHERE name = '송수연'
# """

# cursor.execute(sql)
# db.commit()
# cursor.close()
# db.close()






# <TRY4>

cursor = db.cursor()
sql = """
    SELECT *
        FROM ssy1
"""

cursor.execute(sql)
rs = cursor.fetchall()
print(rs)

# db.commit() # Select문은 검색이기에 필요 없음
cursor.close()
db.close()




