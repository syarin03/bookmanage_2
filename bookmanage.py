import sqlite3

class User():
    def __init__(self):
        self.userid = None
        self.userpw = None
        self.username = None
        self.userphone = None

class Book():
    def __init__(self):
        self.booknum = None
        self.bookname = None
        self.bookwriter = None
        self.bookstatus = 'Possible'


con = sqlite3.connect("book.db", isolation_level=None)

c = con.cursor()

c.execute("SELECT * FROM Books where num = '122968'")

print(c.fetchall()[0][0])

"""
c.execute("UPDATE Books SET publisher = '하랑' where num = '122968'")
con.commit()

c = con.cursor()

c.execute("SELECT * FROM Books where publisher = '아랑'")
"""

con.close()
