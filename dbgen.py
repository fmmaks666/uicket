import sqlite3 as sql

with open("movies.txt") as out:
      TEXT = out.read().splitlines()

db = sql.connect("releases.db")
cursor = db.cursor()
table = """CREATE TABLE IF NOT EXISTS releases(id INTEGER PRIMARY KEY, name TEXT, url TEXT)"""
insert = """INSERT INTO releases(name, url) VALUES(?, ?)"""
ids = (1, 4, 8)
placeholder = ", ".join(["?"] * len(ids))
# what = cursor.execute(f"SELECT name, url FROM releases WHERE id IN({placeholder})", ids)
# print(what.fetchall())
cursor.execute(table)
for i in TEXT:
	name, url = i.split("$")
	cursor.execute(insert, (name, url))
	
db.commit()
db.close()
