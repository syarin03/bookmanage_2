import sqlite3


class User:
    def __init__(self):
        self.userID = None
        self.userPW = None
        self.userName = None
        self.userPhone = None


def login():
    while 1:
        user = User()
        c.execute("SELECT * FROM usertbl")
        print(c.fetchall())
        sel = input("(1) 로그인\n(2) 회원가입\n(3) 아이디/비밀번호 찾기\n(4) 프로그램 종료\n>>> ")
        if sel == '1':
            userlist = c.fetchall()
            inputid = input("아이디\n>>> ")
            inputpw = input("비밀번호\n>>> ")
            for i in userlist:
                if inputid == i[0] and inputpw == i[1]:
                    user.userId = i[0]
                    user.userPW = i[1]
                    user.userName = i[2]
                    user.userPhone = i[3]
                    print("로그인에 성공하셨습니다")
                    # main(user)
                    break
                elif inputid == i[0] and inputpw != i[1]:
                    pass
                else:
                    pass

        elif sel == '2':
            registid = input("id: ")
            registpw = input("pw: ")
            registname = input("name: ")
            registphone = input("phone: ")
            c.execute("select userid from usertbl")
            idlist = c.fetchall()
            print(idlist)

            if len(idlist) == 0:
                print("회원가입에 성공하셨습니다\n")
                c.execute(f"insert into usertbl values('{registid}', '{registpw}', '{registname}', '{registphone}', 0)")

            elif tuple(registid) not in idlist:
                c.execute("SELECT * FROM usertbl ORDER BY userindex DESC")
                cnt = c.fetchall()[0][4] + 1
                print("회원가입에 성공하셨습니다\n")
                c.execute(f"insert into usertbl values('{registid}', '{registpw}', '{registname}', '{registphone}', {cnt})")

            else:
                print("중복된 아이디입니다\n")

        elif sel == '3':
            c.execute("select * from usertbl")
            userlist = c.fetchall()
            temp = input("(1) 아이디 찾기\n(2) 비밀번호 찾기\n(3) 돌아가기\n>>> ")
            if temp == '1':
                inputname = input("name: ")
                inputphone = input("phone: ")
                for i in userlist:
                    if inputname == i[2] and inputphone == i[3]:
                        print(i[0])
                        break
                    elif inputname == i[2] and inputphone != i[3]:
                        pass
                    else:
                        pass

            elif temp == '2':
                inputid = input("id: ")
                inputphone = input("phone: ")
                for i in userlist:
                    if inputid == i[0] and inputphone == i[3]:
                        print(i[1])
                        break
                    elif inputid == i[0] and inputphone != i[3]:
                        pass
                    else:
                        pass
            else:
                pass
        else:
            break


con = sqlite3.connect("book.db", isolation_level=None)
c = con.cursor()
c.execute("")

login()





