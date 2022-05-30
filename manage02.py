import sqlite3

con = sqlite3.connect("book.db",isolation_level=None)

c =con.cursor()

c.execute("SELECT * FROM Books where num = '122955'")

print(c.fetchall())

con.close()