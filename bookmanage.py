import sqlite3


class User():
    def __init__(self):
        self.userID = None
        self.userPW = None
        self.userName = None
        self.userPhone = None
        self.userBook = []


class Book():
    def __init__(self):
        self.bookNum = None
        self.bookName = None
        self.bookWriter = None
        self.bookStatus = 'Possible'


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
