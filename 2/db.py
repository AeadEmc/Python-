import MySQLdb

conn = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='112320',
    db='ph',
)

cur = conn.cursor()

# cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")
sql = "select * from student"
cur.execute(sql)
results = cur.fetchall()
# for rows in results:
#     print(rows)
print(type(results))
print(results)
cur.close()

# conn.commit()


conn.close()
