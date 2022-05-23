import pandas as pd


class User:
    def __init__(self):  # 유사 c언어 구조체
        self.userid = None
        self.pw = None
        self.name = None
        self.add = None

    def setuser(self, userid, pw, name, add):
        self.userid = userid
        self.pw = pw
        self.name = name
        self.add = add

    def printinfo(self):
        print("ID: {0}\nPW: {1}\nNAME: {2}\nADD: {3}".format(self.userid, self.pw, self.name, self.add))


# 도서 목록은 딕셔너리로 고유번호: [저자, 책이름]
f = open("user.txt", 'w')
bookList = pd.read_csv('booklist.csv', encoding='utf-8')
booknum = bookList['등록번호']
bookname = bookList['서명']
bookwriter = bookList['저작자']
print(bookList.shape)
print(bookList)
print('{0} {1} {2}'.format(booknum[1], bookwriter[1], bookname[1]))
cnt = 0
userList = []

while 1:
    sel = input("1. 회원가입\n2. 로그인\n3. ID/PW 찾기\n")
    if sel == '1':
        userList.append("user" + str(cnt))
        userList[cnt] = User()
        userList[cnt].setuser(input("ID: "), input("PW: "), input("NAME: "), input("ADDRESS: "))
        cnt += 1

    for i in userList:
        print("{0}".format(i.printinfo()))


