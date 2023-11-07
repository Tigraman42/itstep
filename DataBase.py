import sqlite3

connection = sqlite3.connect("itstep.sl3", 5)

cur = connection.cursor()


#cur.execute("SELECT rowid, user_name FROM users;")
cur.execute("UPDATE users SET email='new@u.a' where rowid=4;")
connection.commit()

#res = cur.fetchall()
#print(res)

connection.close()