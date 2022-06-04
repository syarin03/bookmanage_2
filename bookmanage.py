from datetime import timedelta
from datetime import datetime
import sqlite3
import random
import os

daycount = 0

class User:  # 회원 정보와 회원 관련 함수를 담을 클래스
    def __init__(self):  # 유사 c언어 구조체
        self.user_id = None
        self.password = None
        self.name = None
        self.phone = None
        self.book = []
        self.cnt2 = None
        self.day = None

    def set_user(self, user_id, password, name, phone, cnt2, day):  # 이건 입력받아서 해당 클래스 변수의 값을 저장하는 함수
        self.user_id = user_id
        self.password = password
        self.name = name
        self.phone = phone
        self.cnt2 = cnt2
        self.day = day

    def printinfo(self):  # 이건 해당 클래스 변수의 값을 출력해주는 함수, 사실 디버깅 용도
        print("아이디: {0} 비밀번호: {1} 이름: {2} 전화번호: {3}".format(
            self.user_id, self.password, self.name, self.phone))

borrow_book = []
end_book = []
rebook = []

con = sqlite3.connect("book.db", isolation_level=None)

c = con.cursor()

def main(nowlogin):
    global daycount
    now = datetime.now()
    borrowday = now
    while True:
        book = []
        c.execute(f"SELECT COUNT(*) FROM renttbl where userid = '{nowlogin.user_id}'")
        if c.fetchall()[0][0] > 0:
            c.execute(f"select rentday, bookid from renttbl")
            for i in c.fetchall():
                c.execute(f"select indexnum, bookname, writer from booktbl where bookid = '{i[1]}'")
                for j in c.fetchall():
                    book += {i + j}
        nowlogin.book = book
        sel = input("(1) 추천 도서\n(2) 도서 조회\n(3) 대여/반납\n(4) 도서 기증\n(5) 내정보\n(6) 로그아웃\n(7) 프로그램 종료\n> ")
        print(sel)
        if sel == '1':
            os.system('clear')
            print("◎ 추천 도서 목록 ◎")
            c.execute("SELECT COUNT(*) FROM booktbl")
            maxnum = int(c.fetchall()[0][0])
            num = list(range(1, maxnum))
            number = []
            for i in range(3):
                number.append(num.pop(num.index(random.choice(num))))
            for i in number:
                c.execute(f"SELECT indexnum, bookname, writer FROM booktbl where bookid == {i}")
                choochun = c.fetchall()
                print(str(choochun[0][0]) + " - " + str(choochun[0][1]) + " - " + str(choochun[0][2]))
        elif sel == '2':
            os.system('clear')
            cho = input("(1) 저자로 검색\n(2) 도서명으로 검색\n(3) 고유번호로 검색\n> ")
            if cho == '1':
                name = input("저자을 입력해주세요.\n> ")
                os.system('clear')
                c.execute(f"SELECT indexnum, bookname, writer FROM booktbl where writer like '%{name}%'")
                if len(c.fetchall()) < 1:
                    print("검색된 도서가 없습니다.")
                else:
                    c.execute(f"SELECT indexnum, bookname, writer FROM booktbl where writer like '%{name}%'")
                    for i in c.fetchall():
                        print(str(i[0]) + " - " + str(i[1]) + " - " + str(i[2]))
            elif cho == '2':
                name = input("도서명을 입력해주세요.\n> ")
                os.system('clear')
                c.execute(f"SELECT indexnum, bookname, writer FROM booktbl where writer like '%{name}%'")
                if len(c.fetchall()) < 1:
                    print("검색된 도서가 없습니다.")
                else:
                    c.execute(f"SELECT indexnum, bookname, writer FROM booktbl where bookname like '%{name}%'")
                    for i in c.fetchall():
                        print(str(i[0]) + " - " + str(i[1]) + " - " + str(i[2]))
            elif cho == '3':
                name = input("고유번호를 입력해주세요.\n> ")
                os.system('clear')
                c.execute(f"SELECT indexnum, bookname, writer FROM booktbl where writer like '%{name}%'")
                if len(c.fetchall()) < 1:
                    print("검색된 도서가 없습니다.")
                else:
                    c.execute(f"SELECT indexnum, bookname, writer FROM booktbl where indexnum like '%{name}%'")
                    for i in c.fetchall():
                        print(str(i[0]) + " - " + str(i[1]) + " - " + str(i[2]))
        elif sel == '3':
            os.system("clear")
            sel2 = input("(1) 대여하기\n(2) 반납하기\n(3) 돌아가기\n> ")
            if sel2 == '1':
                os.system("clear")
                c.execute(f"select rentday from renttbl where userid = '{nowlogin.user_id}'")
                if len(c.fetchall()) == 0:
                    pass
                else:
                    c.execute(f"select rentday from renttbl where userid = '{nowlogin.user_id}'")
                    for i in c.fetchall():
                        if datetime.strptime(i[0], "%Y-%m-%d %H:%M:%S.%f") + timedelta(weeks=1) < now:
                            print("연체중")
                while True:
                    sel3 = input("(1) 고유번호로 대여\n(2) 도서명으로 대여\n(3) 저자명으로 대여\n(4) 대여하기\n(5) 돌아가기\n> ")
                    if sel3 == '1':
                        name = input("고유번호를 입력해주세요.\n> ")
                        os.system("clear")
                        c.execute(f"SELECT indexnum, bookname, writer FROM booktbl where indexnum like '%{name}%'")
                        if len(c.fetchall()) == 0:
                            print("검색된 책이 없습니다.")
                            continue
                        c.execute(f"SELECT indexnum, bookname, writer FROM booktbl where indexnum like '%{name}%'")
                        j = 1
                        for i in c.fetchall():
                            print(str(j) + " - " + str(i[0]) + " - " + str(i[1]) + " - " + str(i[2]))
                            j += 1
                        num = input("원하는 책의 번호를 입력하세요.\n> ")
                        os.system("clear")
                        j = 1
                        c.execute(
                            f"SELECT indexnum, bookname, writer, bookid FROM booktbl where indexnum like '%{name}%'")
                        for i in c.fetchall():
                            if str(j) == num:
                                print(str(i[0]) + " - " + str(i[1]) + " - " + str(i[2]))
                                borrow_book.append((i[0], i[1], i[2], borrowday, i[3]))
                                break
                            j += 1
                        print("장바구니에 담음")
                    elif sel3 == '2':
                        os.system("clear")
                        name = input("도서명을 입력해주세요.\n> ")
                        c.execute(f"SELECT indexnum, bookname, writer FROM booktbl where bookname like '%{name}%'")
                        if len(c.fetchall()) == 0:
                            print("검색된 책이 없습니다.")
                            continue
                        c.execute(f"SELECT indexnum, bookname, writer FROM booktbl where bookname like '%{name}%'")
                        j = 1
                        for i in c.fetchall():
                            print(str(j) + " - " + str(i[0]) + " - " + str(i[1]) + " - " + str(i[2]))
                            j += 1

                        num = input("원하는 책의 번호를 입력하세요.\n> ")
                        os.system("clear")
                        j = 1
                        c.execute(
                            f"SELECT indexnum, bookname, writer, bookid FROM booktbl where bookname like '%{name}%'")
                        for i in c.fetchall():
                            if str(j) == num:
                                print(str(i[0]) + " - " + str(i[1]) + " - " + str(i[2]))
                                borrow_book.append((i[0], i[1], i[2], borrowday, i[3]))
                                break
                            j += 1
                        print("장바구니에 담음")
                    elif sel3 == '3':
                        os.system("clear")
                        name = input("저자명을 입력해주세요.\n> ")
                        c.execute(f"SELECT indexnum, bookname, writer FROM booktbl where writer like '%{name}%'")
                        if len(c.fetchall()) == 0:
                            print("검색된 책이 없습니다.")
                            continue
                        c.execute(f"SELECT indexnum, bookname, writer FROM booktbl where writer like '%{name}%'")
                        j = 1
                        for i in c.fetchall():
                            print(str(j) + " - " + str(i[0]) + " - " + str(i[1]) + " - " + str(i[2]))
                            j += 1

                        num = input("원하는 책의 번호를 입력하세요.\n> ")
                        os.system("clear")
                        j = 1
                        c.execute(
                            f"SELECT indexnum, bookname, writer, bookid FROM booktbl where writer like '%{name}%'")
                        for i in c.fetchall():
                            if str(j) == num:
                                print(str(i[0]) + " - " + str(i[1]) + " - " + str(i[2]))
                                borrow_book.append((i[0], i[1], i[2], borrowday, i[3]))
                                break
                            j += 1
                        print("장바구니에 담음")
                    elif sel3 == '4':
                        os.system("clear")
                        if len(borrow_book) == 0:
                            print("장바구니가 비어있습니다.")
                        else:
                            for i in borrow_book:
                                c.execute(f"SELECT COUNT(*) FROM renttbl where userid = '{nowlogin.user_id}'")
                                if c.fetchall()[0][0] >= 3:
                                    print("3권이상 대여불가")
                                    break
                                else:
                                    c.execute(f"select indexnum, bookname, writer from booktbl where bookid == '{i[4]}'")
                                    j = c.fetchall()[0]
                                    c.execute(f"select * from renttbl where bookid == '{i[4]}'")
                                    if len(c.fetchall()) > 0:
                                        print(str(j[0]) + " - " + str(j[1]) + " - " + str(j[2]))
                                        print("대여중인 도서")
                                        continue
                                    else:
                                        c.execute(f"insert into renttbl values('{nowlogin.user_id}','{now}','{i[4]}')")
                                        print(str(i[0]) + " - " + str(i[1]) + " - " + str(i[2]))
                                        print("대여완료")
                            del borrow_book[:]
                            main(nowlogin)
                    elif sel3 == '5':
                        os.system("clear")
                        print("돌아갑니다.")
                        break
            elif sel2 == '2':
                os.system("clear")
                print("◎ 보유 도서 목록 ◎")
                for i in nowlogin.book:
                    print(i[2] + " - " + i[3] + " - " + i[4])
                if len(nowlogin.book) == 0:
                    print()
                    print("반납할 도서가 없습니다\n")
                    continue
                sel6 = input("(1) 고유번호로 반납\n(2) 도서명으로 반납\n(3) 저자명으로 반납\n(4) 돌아가기\n> ")
                if sel6 == '1':
                    os.system("clear")
                    c.execute(f"SELECT bookid FROM renttbl where userid like '%{nowlogin.user_id}%'")
                    idlist = c.fetchall()
                    for i in idlist:
                        c.execute(f"select bookid, bookname, writer from booktbl where bookid = '{int(i[0])}'")
                        i = c.fetchall()
                        print(str(i[0][0]) + " - " + i[0][1] + " - " + i[0][2])
                    sel7 = input("고유번호를 입력해주세요\n> ")
                    c.execute(f"select * from booktbl where bookid like '%{sel7}%'")
                    ilist = c.fetchall()
                    for i in idlist:
                        os.system("clear")
                        for j in ilist:
                            if int(i[0]) == int(j[0]):
                                c.execute(f"select bookname, writer from booktbl where bookid = '{int(i[0])}'")
                                print(c.fetchall())
                                sel8 = input("반납하시겠습니까?\n(1)o\n(2)x\n> ")
                                if sel8 == '1':
                                    c.execute(f"select rentday from renttbl where userid = '{nowlogin.user_id}'")
                                    for k in c.fetchall():
                                        if datetime.strptime(k[0], "%Y-%m-%d %H:%M:%S.%f") + timedelta(weeks=1) < now:
                                            c.execute(f"UPDATE usertbl set banday = 14 where userid = '{nowlogin.user_id}'")
                                            print("연체됨-14일 대여금지")

                                    c.execute(f"insert into repaytbl values ('{nowlogin.user_id}', '{now}','{i[0]}' )")
                                    c.execute(f"delete from renttbl where bookid = '{int(i[0])}'")
                                if sel8 == '2':
                                    break
                            else:
                                pass
                    os.system("clear")
                    print("반납했습니다.")
                elif sel6 == '2':
                    c.execute(f"SELECT bookid FROM renttbl where userid like '%{nowlogin.user_id}%'")
                    idlist = c.fetchall()
                    print(idlist)
                    for i in idlist:
                        c.execute(f"select bookid, bookname, writer from booktbl where bookid = '{int(i[0])}'")
                        print(c.fetchall())
                    sel7 = input("도서명을 입력해주세요\n> ")
                    c.execute(f"select bookid from booktbl where bookname like '%{sel7}%'")
                    ilist = c.fetchall()
                    for i in idlist:
                        for j in ilist:
                            if int(i[0]) == int(j[0]):
                                print("ok1")
                                c.execute(f"select bookname, writer from booktbl where bookid = '{int(i[0])}'")
                                print(c.fetchall())
                                sel8 = input("지우시겠습니까?,1:o, 2:x")
                                if sel8 == '1':
                                    c.execute(f"select rentday from renttbl where userid = '{nowlogin.user_id}'")
                                    for k in c.fetchall():
                                        print("ok")
                                        if datetime.strptime(k[0], "%Y-%m-%d %H:%M:%S.%f") + timedelta(weeks=1) < now:
                                            c.execute(
                                                f"UPDATE usertbl set banday = 14 where userid = '{nowlogin.user_id}'")
                                            print("연체됨-14일 대여금지")
                                    c.execute(f"insert into repaytbl values ('{nowlogin.user_id}', '{now}', '{int(i[0])}')")
                                    c.execute(f"delete from renttbl where bookid = '{int(i[0])}'")
                                if sel8 == '2':
                                    break
                            else:
                                pass
                    print("반납했습니다.")
                elif sel6 == '3':
                    c.execute(f"SELECT bookid FROM renttbl where userid like '%{nowlogin.user_id}%'")
                    idlist = c.fetchall()
                    print(idlist)
                    for i in idlist:
                        c.execute(f"select bookid, bookname, writer from booktbl where bookid = '{int(i[0])}'")
                        print(c.fetchall())
                    sel7 = input("저자명을 입력해주세요\n> ")
                    c.execute(f"select bookid from booktbl where writer like '%{sel7}%'")
                    ilist = c.fetchall()
                    for i in idlist:
                        for j in ilist:
                            if int(i[0]) == int(j[0]):
                                print("ok1")
                                c.execute(f"select bookname, writer from booktbl where bookid = '{int(i[0])}'")
                                print(c.fetchall())
                                sel8 = input("지우시겠습니까?,1:o, 2:x")
                                if sel8 == '1':
                                    c.execute(f"select rentday from renttbl where userid = '{nowlogin.user_id}'")
                                    for k in c.fetchall():
                                        print("ok")
                                        if datetime.strptime(k[0], "%Y-%m-%d %H:%M:%S.%f") + timedelta(weeks=1) < now:
                                            c.execute(
                                                f"UPDATE usertbl set banday = 14 where userid = '{nowlogin.user_id}'")
                                            print("연체됨-14일 대여금지")
                                    c.execute(f"insert into repaytbl values ('{nowlogin.user_id}', '{now}',{int(i[0])} )")
                                    c.execute(f"delete from renttbl where bookid = '{int(i[0])}'")
                                if sel8 == '2':
                                    break
                            else:
                                pass
                    print("반납했습니다.")
                elif sel6 == '4':
                    os.system("clear")
                    print("돌아갑니다.")
            elif sel2 == '3':
                os.system("clear")
                print("돌아갑니다.")
        elif sel == "4":
            doname = input("기증하실 책의 저자를 입력해주세요\n> ")
            dobook = input("기증하실 도서명을 입력해주세요\n> ")
            dopub = input("기증하실 책의 출판사를 입력해주세요\n> ")
            doyear = input("기증하실 책의 발행년도를 입력해주세요\n> ")
            doplace = input("기증하실 책의 발행지를 입력해주세요.\n> ")
            doprice = input("기증하실 책의 가격을 입력해주세요.\n> ")
            dolibrary = input("기증하실 도서관을 입력해주세요.\n> ")
            c.execute("SELECT COUNT(*) FROM booktbl")
            maxnum = int(c.fetchall()[0][0]) + 1
            c.execute(
                f"insert into booktbl values ({maxnum}, '{dolibrary}', '비치자료', '일반', '1', '{dobook}', '{doname}', '{dopub}', {doyear}, '{doplace}', '원본', {doprice}, '책', '{doname}')")
            os.system("clear")
            print("기증해주셔서 감사합니다.")
        elif sel == '5':
            os.system("clear")
            while True:
                sel01 = input("(1) 대여 중인 도서\n(2) 반납한 도서\n(3) 내정보 변경\n(4) 연체 정보\n(5) 돌아가기\n> ")
                if sel01 == '1':
                    os.system("clear")
                    print("◎ 대여 도서 목록 ◎")
                    c.execute(f"SELECT bookid FROM renttbl where userid = '{nowlogin.user_id}'")
                    idlist = c.fetchall()
                    for i in idlist:
                        c.execute(f"select bookname, writer from booktbl where bookid = '{int(i[0])}'")
                        j = c.fetchall()[0]
                        print(j[0] + " - " + j[1])
                elif sel01 == '2':
                    os.system("clear")
                    print("◎ 반납 도서 목록 ◎")
                    c.execute(f"SELECT bookid FROM repaytbl where userid = '{nowlogin.user_id}'")
                    idlist = c.fetchall()
                    for i in idlist:
                        c.execute(f"select bookname, writer from booktbl where bookid = '{int(i[0])}'")
                        j = c.fetchall()[0]
                        print(j[0] + " - " + j[1])
                elif sel01 == '3':
                    os.system("clear")
                    sel02 = input("(1) 아이디 변경\n(2) 비밀번호 변경\n(3) 이름 변경\n(4) 전화번호 변경\n> ")
                    if sel02 == '1':
                        os.system("clear")
                        sel09 = input("변경할 아이디를 입력해주세요\n")
                        c.execute(f"update renttbl set userid = '{sel09}' where userid = '{nowlogin.user_id}'")
                        c.execute(f"update repaytbl set userid = '{sel09}' where userid = '{nowlogin.user_id}'")
                        c.execute(f"update usertbl set userid = '{sel09}' where userid = '{nowlogin.user_id}'")
                        nowlogin.user_id = sel09
                        print("변경된 아이디", sel09)
                    elif sel02 == '2':
                        os.system("clear")
                        sel10 = input("변경할 비밀번호를 입력해주세요\n")
                        c.execute(f"update usertbl set userpw = '{sel10}' where userid = '{nowlogin.user_id}'")
                        print("변경된 비밀번호", sel10)
                        nowlogin.password = sel10
                    elif sel02 == '3':
                        os.system("clear")
                        sel11 = input("변경할 이름을 입력해주세요\n")
                        c.execute(f"update usertbl set username = '{sel11}' where userid = '{nowlogin.user_id}'")
                        print("변경된 이름", sel11)
                        nowlogin.name = sel11
                    elif sel02 == '4':
                        os.system("clear")
                        sel12 = input("변경할 전화번호를 입력해주세요\n")
                        c.execute(f"update usertbl set userphone = '{sel12}' where userid = '{nowlogin.user_id}'")
                        print("변경된 번호", sel12)
                        nowlogin.phone = sel12
                elif sel01 == '4':
                    os.system("clear")
                    print("◎ 연체 도서 목록 ◎")
                    c.execute(f"select rentday, bookid from renttbl  where userid = '{nowlogin.user_id}'")
                    for i in c.fetchall():
                       if datetime.strptime(i[0], "%Y-%m-%d %H:%M:%S.%f") + timedelta(weeks=1) < now:
                            c.execute(f"select bookname from booktbl where bookid = '{i[1]}'")
                            print(c.fetchall()[0][0])
                    c.execute(f"select banday from usertbl where userid = '{nowlogin.user_id}'")
                    print("대여금지 남은기간" + " " + c.fetchall()[0][0])
                elif sel01 == '5':
                    os.system("clear")
                    print("돌아갑니다.")
                    break
        elif sel == '6':
            os.system("clear")
            print("로그아웃합니다.")
            login()
        elif sel == '7':
            os.system("clear")
            print("프로그램을 종료합니다\n")
            exit(0)
        elif sel == '8':
            os.system("clear")
            daycount += 1
            now = datetime.now() + timedelta(days=daycount)
            c.execute(f"select banday from usertbl where userid = '{nowlogin.user_id}'")
            if int(c.fetchall()[0][0]) > 0:
                c.execute(f"UPDATE usertbl set banday = banday - 1")
            print(now)
            print("다음날\n")

userList = []

def login():
    while 1:
        user = User()
        c.execute("SELECT * FROM usertbl")
        userlist = c.fetchall()
        sel11 = input("(1) 로그인\n(2) 회원가입\n(3) 아이디/비밀번호 찾기\n(4) 프로그램 종료\n>>> ")
        if sel11 == '1':
            inputid = input("아이디\n>>> ")
            inputpw = input("비밀번호\n>>> ")
            for i in userlist:
                if inputid == i[0] and inputpw == i[1]:
                    user.user_id = i[0]
                    user.password = i[1]
                    user.name = i[2]
                    user.phone = i[3]
                    os.system('clear')
                    print("로그인에 성공하셨습니다.")
                    main(user)
                    break
                elif inputid == i[0] and inputpw != i[1]:
                    os.system('clear')
                    print("비밀번호를 다시 입력해주세요.")
                    break
                else:
                    os.system('clear')
                    print("로그인에 실패하였습니다.")
                    pass
        elif sel11 == '2':
            os.system('clear')
            registid = input("id: ")
            registpw = input("pw: ")
            registname = input("name: ")
            registphone = input("phone: ")
            c.execute("select userid from usertbl")
            idlist = c.fetchall()
            if len(idlist) == 0:
                os.system('clear')
                print("회원가입에 성공하셨습니다\n")
                c.execute(f"insert into usertbl values('{registid}', '{registpw}', '{registname}', '{registphone}', 0, 0)")
            elif tuple(registid) not in idlist:
                os.system('clear')
                c.execute("SELECT * FROM usertbl ORDER BY userindex DESC")
                cnt = int(c.fetchall()[0][4] + 1)
                print("회원가입에 성공하셨습니다\n")
                c.execute(
                    f"insert into usertbl values('{registid}', '{registpw}', '{registname}', '{registphone}', {cnt}, 0)")
            else:
                os.system('clear')
                print("중복된 아이디입니다\n")
        elif sel11 == '3':
            os.system('clear')
            c.execute("select * from usertbl")
            userlist = c.fetchall()
            temp = input("(1) 아이디 찾기\n(2) 비밀번호 찾기\n(3) 돌아가기\n>>> ")
            if temp == '1':
                os.system('clear')
                inputname = input("name: ")
                inputphone = input("phone: ")
                for i in userlist:
                    if inputname == i[2] and inputphone == i[3]:
                        print(i[0])
                        break
                    else:
                        os.system('clear')
                        print("등록되지 않은 사용자입니다.")
                        pass
            elif temp == '2':
                inputid = input("아이디\n>>> ")
                inputphone = input("전화번호\n>>> ")
                for i in userlist:
                    if inputid == i[0] and inputphone == i[3]:
                        print(i[1])
                        break
                    else:
                        os.system('clear')
                        print("정보를 잘못 입력하였습니다.")
                        pass
            else:
                pass
        elif sel11 == '4':
            os.system('clear')
            print("프로그램을 종료합니다.")
            exit(0)
        else:
            pass

login()