import sqlite3

db = sqlite3.connect(GPU.db)
cursor = db.cursor()
sql = "SELECT * from gpu;"
cursor.execute(sql)
results = cursor.fetchall()
print(results)


db.close()
