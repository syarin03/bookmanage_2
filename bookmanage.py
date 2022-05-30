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

"""
c.execute("SELECT * FROM booktbl where bookid = '122968'")
print(c.fetchall()[0])

c.execute("SELECT * FROM booktbl where pubplace = '인천'")
print(len(c.fetchall()))

c.execute("SELECT * FROM booktbl where bookname like '%베르%'")
print(len(c.fetchall()))

c.execute("SELECT * FROM booktbl where bookname like '%베르%'")
for i in c.fetchall():
    print(i[5] + " <> " + i[6])
    
c.execute("SELECT * FROM booktbl where bookname like '%"+temp+"%'")
for i in c.fetchall():
    print(i[5] + " <> " + i[6])
"""

temp = input()


c.execute("SELECT bookname, writer, lib FROM booktbl where bookname like '%"+temp+"%' and isrent = 0")
for i in c.fetchall():
    print(i[0] + " <> " + i[1] + " <> " + i[2])

"""
c.execute("UPDATE Books SET publisher = '하랑' where num = '122968'")
con.commit()

c = con.cursor()

c.execute("SELECT * FROM Books where publisher = '아랑'")
"""

con.close()
