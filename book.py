from datetime import datetime, timedelta
import sqlite3
import random
import os
import time


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
daycount = 0


def main(nowlogin, daycount):
    now = datetime.now() - timedelta(weeks=1)
    borrowday = now
    while True:
        sel = input("(1) 추천 도서\n(2) 도서 조회\n(3) 대여/반납\n(4) 도서 기증\n(5) 내정보\n(6) 로그아웃\n(7) 프로그램 종료\n> ")
        if sel == '1':
            print("◎ 추천 도서 목록 ◎\n")
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
            cho = input("(1) 저자로 검색\n(2) 도서명으로 검색\n(3) 고유번호로 검색\n> ")
            if cho == '1':
                name = input("저자을 입력해주세요.\n> ")
                c.execute(f"SELECT indexnum, bookname, writer FROM booktbl where writer like '%{name}%'")
                for i in c.fetchall():
                    print(str(i[0]) + " - " + str(i[1]) + " - " + str(i[2]))
            elif cho == '2':
                name = input("도서명을 입력해주세요.\n> ")
                c.execute(f"SELECT indexnum, bookname, writer FROM booktbl where bookname like '%{name}%'")
                for i in c.fetchall():
                    print(str(i[0]) + " - " + str(i[1]) + " - " + str(i[2]))
            elif cho == '3':
                name = input("고유번호를 입력해주세요.\n> ")
                c.execute(f"SELECT indexnum, bookname, writer FROM booktbl where indexnum like '%{name}%'")
                for i in c.fetchall():
                    print(str(i[0]) + " - " + str(i[1]) + " - " + str(i[2]))
        elif sel == '3':
            sel2 = input("(1) 대여하기\n(2) 반납하기\n> ")
            if sel2 == '1':
                for i in nowlogin.book:
                    if i[3] + timedelta(weeks=1) < now:
                        print("연체중")
                        break
                if nowlogin.day < now:
                    print("대여금지중")
                    main(nowlogin, daycount)
                while True:
                    sel3 = input("(1) 고유번호로 대여\n(2) 도서명으로 대여\n(3) 저자명으로 대여\n(4) 대여하기\n> ")
                    if sel3 == '1':
                        name = input("고유번호를 입력해주세요.\n> ")
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
                        j = 1
                        c.execute(f"SELECT indexnum, bookname, writer FROM booktbl where indexnum like '%{name}%'")
                        for i in c.fetchall():
                            if str(j) == num:
                                print(str(i[0]) + " - " + str(i[1]) + " - " + str(i[2]))
                                borrow_book.append((i[0], i[1], i[2], borrowday))
                                break
                            j += 1
                        print("장바구니에 담음")
                    elif sel3 == '2':
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
                        j = 1
                        c.execute(f"SELECT indexnum, bookname, writer FROM booktbl where bookname like '%{name}%'")
                        for i in c.fetchall():
                            if str(j) == num:
                                print(str(i[0]) + " - " + str(i[1]) + " - " + str(i[2]))
                                borrow_book.append(i)
                                break
                            j += 1
                        print("장바구니에 담음")
                    elif sel3 == '3':
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
                        j = 1
                        c.execute(f"SELECT indexnum, bookname, writer FROM booktbl where writer like '%{name}%'")
                        for i in c.fetchall():
                            if str(j) == num:
                                print(str(i[0]) + " - " + str(i[1]) + " - " + str(i[2]))
                                borrow_book.append(i)
                                break
                            j += 1
                        print("장바구니에 담음")
                    elif sel3 == '4':
                        nowlogin.book += borrow_book
                        for i in nowlogin.book:
                            c.execute(f"insert into renttbl values('{nowlogin.user_id}','{now}','{i[0]}')")

                        for i in borrow_book:
                            print(str(i[0]) + " - " + str(i[1]) + " - " + str(i[2]))
                        print("대여완료")
                        del borrow_book[:]
                        print(borrow_book)  # 확인용
                        break
            elif sel2 == '2':
                if len(nowlogin.book) == 0:
                    print()
                    print("반납할 도서가 없습니다\n")
                    continue
                sel6 = input("(1) 고유번호로 반납\n(2) 도서명으로 반납\n(3) 저자명으로 반납\n")
                if sel6 == '1':
                    for i in nowlogin.book:
                        print(str(i[0]) + " - " + str(i[1]) + " - " + str(i[2]))
                    sel7 = input("고유번호를 입력해주세요\n> ")
                    j = 1
                    for i in nowlogin.book:
                        if i[0].find(sel7) != -1:
                            print(str(j) + " - " + str(i[0]) + " - " + str(i[1]) + " - " + str(i[2]))
                        j += 1
                    repay = input("반납할 책의 번호를 입력해주세요.")
                    j = 1
                    for i in nowlogin.book:
                        if i[0].find(sel7) != -1 and repay == str(j):
                            print(str(i[0]) + " - " + str(i[1]) + " - " + str(i[2]))
                            if i[3] + timedelta(weeks=1) < now:
                                print("ok")
                                print(nowlogin.day + timedelta(weeks=2))
                                print("연체함")
                            nowlogin.book.remove(i)
                            rebook.append(i)
                            print("반납하였습니다.")
                            return nowlogin.day
                        j += 1
                elif sel6 == '2':
                    for i in nowlogin.book:
                        print(str(i[0]) + " - " + str(i[1]) + " - " + str(i[2]))
                    sel7 = input("도서명을 입력해주세요\n> ")
                    j = 1
                    for i in nowlogin.book:
                        if i[1].find(sel7):
                            print(str(j) + " - " + str(i[0]) + " - " + str(i[1]) + " - " + str(i[2]))
                        j += 1
                    repay = input("반납할 책의 번호를 입력해주세요.")
                    j = 1
                    for i in nowlogin.book:
                        if i[1].find(sel7) and repay == str(j):
                            print(str(i[0]) + " - " + str(i[1]) + " - " + str(i[2]))
                            rebook.append(i)
                            print("반납하였습니다.")
                            nowlogin.book.remove(i)
                            break
                        j += 1
                elif sel6 == '3':
                    for i in nowlogin.book:
                        print(str(i[0]) + " - " + str(i[1]) + " - " + str(i[2]))
                    sel7 = input("작가명을 입력해주세요\n> ")
                    j = 1
                    for i in nowlogin.book:
                        if i[2].find(sel7):
                            print(str(j) + " - " + str(i[0]) + " - " + str(i[1]) + " - " + str(i[2]))
                        j += 1
                    repay = input("반납할 책의 번호를 입력해주세요.")
                    j = 1
                    for i in nowlogin.book:
                        if i[2].find(sel7) and repay == str(j):
                            print(str(i[0]) + " - " + str(i[1]) + " - " + str(i[2]))
                            rebook.append(i)
                            print("반납하였습니다.")
                            nowlogin.book.remove(i)
                            break
                        j += 1
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
                f"insert into booktbl values ({maxnum}, '{dolibrary}', '비치자료', '일반', '1', '{dobook}', '{doname}', '{dopub}', {doyear}, '{doplace}', '원본', {doprice}, '책', '{doname}', '1')")
        elif sel == '5':
            while True:
                nowlogin.printinfo()
                sel01 = input("(1) 대여 중인 도서\n(2) 반납한 도서\n(3) 내정보 변경\n(4) 연체 정보\n(5) 돌아가기\n> ")
                if sel01 == '1':
                    print("대여 중인 도서: ", nowlogin.book)
                elif sel01 == '2':
                    print("반납한 도서: ", rebook)
                elif sel01 == '3':
                    sel02 = input("(1) 아이디 변경\n(2) 비밀번호 변경\n(3) 이름 변경\n(4) 전화번호 변경\n> ")
                    if sel02 == '1':
                        change_id = input("변경할 아이디를 입력해주세요\n> ")
                        nowlogin.user_id = change_id
                        print("변경된 아이디: ", nowlogin.user_id)
                    elif sel02 == '2':
                        change_pw = input("변경할 비밀번호를 입력해주세요\n> ")
                        nowlogin.password = change_pw
                        print("변경된 비밀번호: ", nowlogin.password)
                    elif sel02 == '3':
                        change_name = input("바꿀 이름 입력\n> ")
                        nowlogin.name = change_name
                        print("변경된 이름: ", nowlogin.name)
                    elif sel02 == '4':
                        change_phone = input("바꿀 번호 입력 \n> ")
                        nowlogin.phone = change_phone
                        print("변경된 전화번호: ", nowlogin.phone)
                elif sel01 == '4':
                    print("연체된 책")
                    for i in nowlogin.book:
                        if i[3] + timedelta(weeks=1) < now:
                            print(i)
                elif sel01 == '5':
                    break
        elif sel == '6':
            print("로그아웃합니다.")
            return daycount
        elif sel == '7':
            print("프로그램을 종료합니다\n")
            exit(0)
        elif sel == '8':
            daycount += 1
            now = datetime.now() + timedelta(days=daycount)
            print(daycount)
            print(now)
            print("다음날\n")
        elif sel == '0':
            c.execute("SELECT * FROM booktbl")
            print(c.fetchall())


cnt = 0
userList = []

while True:
    sel = input("(1) 회원가입\n(2) 로그인\n(3) ID/PW 찾기\n(4) 프로그램 종료\n> ")
    if sel == '1':
        registok = True
        userid = input("아이디\n> ")
        password = input("비밀번호\n> ")
        name = input("이름\n> ")
        phone = input("전화번호\n> ")
        if len(userList) != 0:
            for i in userList:
                if i.user_id == userid:
                    print("중복된 아이디입니다\n")
                    registok = False
                    break
                else:
                    registok = True
        if registok:
            userList.append("user" + str(cnt))  # 회원정보 리스트에 값 추가하기
            userList[cnt] = User()  # 해당 요소를 User 클래스로 만들어주기
            userList[cnt].set_user(userid, password, name, phone, 0, datetime.now())  # input을 통해 값을 입력받고 각각 값으로 저장
            print()

            print("회원가입이 완료되었습니다\n")
            cnt += 1  # 이건 리스트 인덱스 때문에 늘려주는 것


    elif sel == '2':
        loop = True  # 단순 while문을 돌리기 위한 변수
        while loop:
            if len(userList) == 0:
                print("등록된 회원 정보가 존재하지 않습니다\n회원가입 먼저 해주세요\n")
                break
            userid = input("ID\n> ")
            pw = input("PW\n> ")
            for i in userList:  # 유저 리스트로 반복문을 굴리면서
                wrong_id = False  # 미리 false로 해둔 이유는 로그인 정보가 일치하지 않을 때의 값을 true로 두기 위해서
                if i.user_id == userid:  # 입력받은 아이디와 같은 아이디가 리스트 내에 있는지 확인하고
                    if i.password == pw:  # 여기서 비번까지 맞다면
                        nowlogin = i
                        daycount = main(i, daycount)  # 메인화면 함수를 불러오는 것
                        loop = False  # while문을 종료시켜야 하기 때문에 false로 바꿔주고
                        break  # 해당 for문 또한 종료
                    else:  # 이건 아이디는 있는데 비번이 잘못됐을 경우
                        print("비밀번호를 잘못 입력하셨습니다\n")
                        break  # 해당 for문 또한 종료
                    wrong_id = False  # 얘는 계속 아이디가 틀린 게 아닌 이상 늘 false여야 하기 때문에 재차 초기화 해주는거고
                else:  # 이건 아이디가 등록되어 있지 않은 경우, 틀린 경우도 포함이겠죠
                    wrong_id = True
            if wrong_id:  # 여기서 아이디가 있는지 없는지 확인하고 없다면
                print("존재하지 않는 아이디입니다\n")  # 존재하지 않는다고 알려주기
    elif sel == '3':
        if len(userList) == 0:
            print("등록된 회원 정보가 존재하지 않습니다\n회원가입 먼저 해주세요\n")
            continue
        loop = True
        while loop:
            find_sel = input("(1) 아이디 찾기\n(2) 비밀번호 찾기\n(3) 돌아가기\n> ")
            if find_sel == '1':
                for i in userList:
                    if input("이름 입력\n> ") == i.name:
                        if input("연락처 입력\n> ") == i.phone:
                            print("ID: {0}".format(i.user_id))
                        else:
                            print("입력하신 연락처 정보가 존재하지 않습니다\n")
                    else:
                        print("입력하신 이름의 계정이 존재하지 않습니다\n")
                    break
            elif find_sel == '2':
                for i in userList:
                    if input("아이디 입력\n> ") == i.user_id:
                        if input("전화번호 입력\n> ") == i.phone:
                            print("PW: {0}".format(i.password))
                        else:
                            print("입력하신 연락처 정보가 존재하지 않습니다\n")
                    else:
                        print("입력하신 아이디가 존재하지 않습니다\n")
                    break
            elif find_sel == '3':
                print("선택 화면으로 돌아갑니다\n")
                break
    elif sel == '4':
        print("프로그램을 종료합니다\n")
        exit(0)