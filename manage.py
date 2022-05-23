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
        print("ID:{0} PW:{1} NAME:{2} ADD:{3}".format(self.userid, self.pw, self.name, self.add))


# 도서 목록은 딕셔너리로 고유번호: [저자, 책이름]
cnt = 0
userList = []

while 1:
    sel = input("1. 회원가입\n2. 로그인\n3. ID/PW 찾기\n")
    if sel == '1':
        userList.append("user" + str(cnt))
        userList[cnt] = User()
        userList[cnt].setuser(input("ID: "), input("PW: "), input("NAME: "), input("ADDRESS: "))
        cnt += 1

    if sel == '2':
        idfalse = False
        loop = True
        while loop:
            userid = input("ID: ")
            pw = input("PW: ")
            for i in userList:
                if i.userid == userid:
                    idfalse = False
                    if i.pw == pw:
                        loop = False
                        break
                    else:
                        print("비밀번호가 잘못 입력되었습니다.")
                else:
                    idfalse = True
            if idfalse:
                print("존재하지 않는 아이디입니다.")

    for i in userList:
        print("{0}".format(i.printinfo()))
