import random

class User:  # 회원 정보와 회원 관련 함수를 담을 클래스
    def __init__(self):  # 유사 c언어 구조체
        self.user_id = None
        self.password = None
        self.name = None
        self.phone = None
        self.book = []
        self.book_cnt = None

    def set_user(self, user_id, password, name, phone, book_cnt):  # 이건 입력받아서 해당 클래스 변수의 값을 저장하는 함수
        self.user_id = user_id
        self.password = password
        self.name = name
        self.phone = phone
        self.book_cnt = book_cnt

    def printinfo(self):  # 이건 해당 클래스 변수의 값을 출력해주는 함수, 사실 디버깅 용도
        print("아이디: {0}\n비밀번호: {1}\n이름: {2}\n전화번호: {3}\n대여 중인 도서: {4}\n대여 중인 도서 개수: {5}\n".format(
            self.user_id, self.password, self.name, self.phone, self.book, self.book_cnt))


dic = {"001": ["황순원", "별", "대여가능"], "002": ["이광수", "흙", "대여가능"], "003": ["나도향", "벙어리삼룡이", "대여가능"], "004": ["전영택", "화수분", "대여가능"],
       "005": ["김유정", "동백꽃", "대여가능"], "006": ["피터 스완슨", "여덟 건의 완벽한 살인", "대여가능"], "007": ["오노 후유미", "시귀1", "대여가능"],
       "008": ["나가츠키 탓페이", "Re:제로부터 시작하는 이세계 생활", "대여가능"], "009": ["베르나르 베르베르", "파피용", "대여가능"], "010": ["정찬주", "공부하다 죽어라", "대여가능"]}
borrow_book = []
end_book = []
rebook = []

def main(nowlogin):  # 로그인 성공 후 메인화면
    cnt1 = 0
    while True:
        sel = input("(1) 추천 도서\n(2) 도서 조회\n(3) 대여/반납 현황\n(4) 도서 기증\n(5) 마이페이지\n(6) 로그아웃\n(7) 끝내기\n> ")
        if sel == '1':
            maxnum = int(list(dic.keys())[-1])+1
            num = list(range(1, maxnum))  # num = [1,2,3,4,5,6,7,8,9,10]
            number = []  # 리스트선언
            for i in range(3):  # 3번반복
            # random.choice(num)으로 1~10중 랜덤한 값을 추출한 뒤, num.index로 해당 값의 위치를 추출하고, num.pop로 해당 위치의 값을 추출한 뒤 리스트에서 삭제한 후, number.append를 통해서 리스트에 3번 대입
                number.append(num.pop(num.index(random.choice(num)))-1)
            #print(f'{"추천도서목록":=^40}')
            #print(f'{"저자":^20}'+f'{"도서명":^20}')
            for i in range(3):
                print(list(dic.values())[number[i]][0] + " - " + list(dic.values())[number[i]][1])
        elif sel == '2':
            cho = input("(1) 저자로 검색\n(2) 도서명으로 검색\n(3) 고유번호로 검색\n> ")
            if cho == '1':
                name = input("작가명을 입력해주세요.\n> ")
                for i in dic.values():
                    if i[0].find(name) != -1:
                        print(i[0] + " - " + i[1])
                    else:
                        pass
            elif cho == '2':
                bookname = input("책이름을 입력해주세요.\n> ")
                for i in dic.values():
                    if i[1].find(bookname) != -1:
                        print(i[0] + " - " + i[1])
                    else:
                        pass
            elif cho == '3':
                booknum = input("고유번호를 입력해주세요.\n> ")
                for i in dic.keys():
                    if i.find(booknum) != -1:
                        print(dic.get(i)[0] + " - " + dic.get(i)[1])
                    else:
                        pass
        elif sel == '3':
            sel2 = input("(1) 대여\n(2) 반납\n> ")
            if sel2 == '1':
                while True:
                    sel3 = input("(1) 고유번호로 대여\n(2) 도서명으로 대여\n(3) 대여하기\n> ")
                    if sel3 == '1':
                        booknum = input("고유번호를 입력해주세요.\n> ") # 책의 고유번호를 사용해서 검색하는 부분
                        for i in dic.keys():
                            if i.find(booknum) != -1:
                                print( i + " - " + dic.get(i)[0] + " - " + dic.get(i)[1]) # 검색해서 출력해주는 부분
                            else:
                                pass
                        sel4 = input("원하는 책의 고유번호를 입력해주세요.\n> ")
                        if ((dic[sel4][2])) == "대여 가능" and cnt1 < 3 and nowlogin.book_cnt < 3:
                            borrow_book.append([sel4, dic[sel4][0], dic[sel4][1]])
                            ((dic[sel4][2])) = nowlogin.user_id
                            cnt1 += 1
                            print(dic[sel4][2])
                            print("대여한 도서:", borrow_book)
                        else:
                            print("대여가 불가능한 도서입니다.\n")
                    elif sel3 == '2':
                        bookname = input("책이름을 입력해주세요.\n> ")
                        for i in dic.values():
                            if i[1].find(bookname) != -1:
                                print(i[0] + " - " + i[1])
                            else:
                                pass
                        selbook = input("원하는 책의 이름을 입력해주세요.\n> ")
                        for i in list(dic.values()):
                            if selbook == i[1] and i[2] == "대여가능" and cnt1<3 and nowlogin.book_cnt<3:
                                for j in dic.keys():
                                    if dic[j] == i:
                                        cnt1 += 1
                                        borrow_book.append([j, i[0], i[1]])
                                        i[2] = nowlogin.user_id
                                        print(i[0],i[1])
                                        print(borrow_book)
                    elif sel3 == '3':
                        nowlogin.book += borrow_book
                        print(borrow_book)
                        nowlogin.book_cnt += cnt1
                        cnt1 = 0
                        print("도서를 대여하였습니다.\n")
                        print(nowlogin.book_cnt)
                        print(dic)

                        del borrow_book[:]
                        break
            if sel2 == '2':
                sel6 = input("(1) 번호로 반납\n(2) 이름으로 반납\n> ")
                # 반납 리스트에 아무것도 없으면 바로 빠꾸 먹이기
                if sel6 == '1':
                    print(nowlogin.book)
                    sel7 = input("도서번호 입력\n> ")
                    for j in nowlogin.book:  # 사용자가 가지고 있는 책리스트의 첫번째부터 서치
                        for i in dic.values():
                            if i == dic[sel7] and i[:2] == j[1:]: # 001의 value가 입력한 키의 value와 같고, 해당 value의 0번,1번이 해당 nowlogin.book의 첫번째와 같을 때
                                rebook.append(j)
                                nowlogin.book.remove(j)
                                i[2] = "대여가능"
                    print(rebook)
                    print(nowlogin.book)
                    if nowlogin.book_cnt > 0:
                        nowlogin.book_cnt -= 1

                if sel6 == '2':
                    print(nowlogin.book)
                    set8 = input("책 이름 입력\n> ")
                    for j in dic.keys():
                        if dic[j][1].find(set8) != -1: # i = [작가, 책이름, 상태], nowlogin.book = [[작가, 책이름],[작가, 책이름],[작가, 책이름]...]
                            cnt1 = 0
                            print(dic[j][0:2])
                            rebook.append(dic[j][0:2])
                            nowlogin.book.remove([j, dic[j][0], dic[j][1]])
                            dic[j][2] = "대여가능"
                    print(nowlogin.book)
                    if nowlogin.book_cnt > 0:
                        nowlogin.book_cnt -= 1

            if sel2 == '3':
                print("반납된 도서:", end_book)


        elif sel == '4':
            doname = input("기증하실 책의 작가명을 입력해주세요\n> ")
            dobook = input("기증하실 책의 이름을 입력해주세요\n> ")
            keynum = "0"+str(int(list(dic.keys())[-1])+1)
            dic.update({keynum:[doname, dobook]})
        elif sel == '5':
            nowlogin.printinfo()
            sel01 = input("(1) 대여 중인 도서\n(2) 반납한 도서\n(3) 연체 도서\n(4) 내정보변경\n(5) 연체 정보\n> ")
            if sel01 == '1':
                print("대여 중인 도서: ", nowlogin.book)
            if sel01 == '2':
                print("반납한 도서:", rebook)
            if sel01 == '3':
                pass
            if sel01 == '4':
                sel02 = input("(1) 아이디 변경\n(2) 비밀번호 변경\n(3) 이름 변경\n(4) 전화번호 변경\n> ")
                if sel02 == '1':
                    change_id = input("변경할 아이디 입력\n> ")
                    nowlogin.user_id = change_id
                    print("변경된 아이디", nowlogin.user_id)
                if sel02 == '2':
                    change_pw = input("변경할 비밀번호 입력\n> ")
                    nowlogin.password = change_pw
                    print("변경된 비밀번호", nowlogin.password)
                if sel02 == '3':
                    change_name = input("변경할 이름 입력\n> ")
                    nowlogin.name = change_name
                    print("변경된 이름", nowlogin.name)
                if sel02 == '4':
                    change_phone = input("변경할 번호 입력\n> ")
                    nowlogin.phone = change_phone
                    print("변경된 전화번호", nowlogin.phone)
        elif sel == '6':
            break
        elif sel == '7':
            print("프로그램을 종료합니다\n")
            exit(0)
        elif sel == '0': #테스트용
            print(dic.items())

cnt = 0
userList = []  # 여기에 회원정보를 리스트로 담을 예정

while 1:
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
                    print("중복된 아이디입니다.\n")
                    registok = False
                    break
                else:
                    registok = True
        if registok:
            userList.append("user" + str(cnt))  # 회원정보 리스트에 값 추가하기
            userList[cnt] = User()  # 해당 요소를 User 클래스로 만들어주기
            userList[cnt].set_user(userid, password, name, phone, 0)  # input을 통해 값을 입력받고 각각 값으로 저장
            print("회원가입이 완료되었습니다.\n")
            cnt += 1  # 이건 리스트 인덱스 때문에 늘려주는 것
        

    elif sel == '2':
        loop = True  # 단순 while문을 돌리기 위한 변수
        while loop:
            if len(userList) == 0:
                print("등록된 회원 정보가 존재하지 않습니다.\n회원가입 먼저 해주세요\n")
                break
            userid = input("ID\n> ")
            pw = input("PW\n> ")
            for i in userList:  # 유저 리스트로 반복문을 굴리면서
                wrong_id = False  # 미리 false로 해둔 이유는 로그인 정보가 일치하지 않을 때의 값을 true로 두기 위해서
                if i.user_id == userid:  # 입력받은 아이디와 같은 아이디가 리스트 내에 있는지 확인하고
                    if i.password == pw:  # 여기서 비번까지 맞다면
                        print("로그인에 성공하였습니다.\n")  # 성공 메세지 띄우고
                        nowlogin = i
                        main(i)  # 메인화면 함수를 불러오는 것
                        loop = False  # while문을 종료시켜야 하기 때문에 false로 바꿔주고
                        break  # 해당 for문 또한 종료
                    else:  # 이건 아이디는 있는데 비번이 잘못됐을 경우
                        print("비밀번호가 잘못 입력되었습니다.\n")
                        break  # 해당 for문 또한 종료
                    wrong_id = False  # 얘는 계속 아이디가 틀린 게 아닌 이상 늘 false여야 하기 때문에 재차 초기화 해주는거고
                else:  # 이건 아이디가 등록되어 있지 않은 경우, 틀린 경우도 포함이겠죠
                    wrong_id = True
            if wrong_id:  # 여기서 아이디가 있는지 없는지 확인하고 없다면
                print("존재하지 않는 아이디입니다.\n")  # 존재하지 않는다고 알려주기
    elif sel == '3':
        if len(userList) == 0:
            print("등록된 회원 정보가 존재하지 않습니다.\n회원가입 먼저 해주세요\n")
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
                            print("입력하신 연락처 정보가 존재하지 않습니다.\n")
                    else:
                        print("입력하신 이름의 계정이 존재하지 않습니다.\n")
                    break
            elif find_sel == '2':
                for i in userList:
                    if input("아이디 입력\n> ") == i.user_id:
                        if input("전화번호 입력\n> ") == i.phone:
                            print("PW: {0}".format(i.password))
                        else:
                            print("입력하신 연락처 정보가 존재하지 않습니다.\n")
                    else:
                        print("입력하신 아이디가 존재하지 않습니다.\n")
                    break
            elif find_sel == '3':
                print("선택 화면으로 돌아갑니다\n")
                break
    elif sel == '4':
        print("프로그램을 종료합니다\n")
        exit(0)
    """
    for i in userList:  # 이건 그냥 단순히 디버깅 용도로 회원 리스트 출력해주는 것
        print("{0}".format(i.print_info()))
    """