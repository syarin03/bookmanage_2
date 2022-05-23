class User:  # 회원 정보와 회원 관련 함수를 담을 클래스
    def __init__(self):  # 유사 c언어 구조체
        self.userid = None
        self.pw = None
        self.name = None
        self.add = None

    def setuser(self, userid, pw, name, add):  # 이건 입력받아서 해당 클래스 변수의 값을 저장하는 함수
        self.userid = userid
        self.pw = pw
        self.name = name
        self.add = add

    def printinfo(self):  # 이건 해당 클래스 변수의 값을 출력해주는 함수, 사실 디버깅 용도
        print("ID:{0} PW:{1} NAME:{2} ADD:{3}".format(self.userid, self.pw, self.name, self.add))


def main():  # 로그인 성공 후 메인화면
    sel = input("1. 추천 도서\n2. 도서 조회\n3. 대여/반납 현황\n4. 도서 기증\n5. 마이페이지")


# 도서 목록은 딕셔너리로 {고유번호: [저자, 책이름]}
"""
dic = {"001": ["저자", "책이름"], "002": ["저자", "책이름"]}  # 대충 요런식
print(dic)  # 이건 딕셔너리 전체
print(dic['001'])  # 이건 해당 key의 value 불러오기
for i in dic:
    print(i)  # key, 그러니까 도서 고유번호 불러올 때
    print(dic.get(str(i)))  # 이건 key의 value, 저자와 도서명을 불러올 때
    print(dic.get(str(i))[0])
    print(dic.get(str(i))[1])  # 이런 식으로 value 내 리스트 값 단일로 뽑아내기 가능
"""
cnt = 0
userList = []  # 여기에 회원정보를 리스트로 담을 예정

while 1:
    sel = input("1. 회원가입\n2. 로그인\n3. ID/PW 찾기\n")
    if sel == '1':
        userList.append("user" + str(cnt))  # 회원정보 리스트에 값 추가하기
        userList[cnt] = User()  # 해당 요소를 User 클래스로 만들어주기
        userList[cnt].setuser(input("ID: "), input("PW: "), input("NAME: "), input("ADDRESS: "))  # input을 통해 값을 입력받고 각각 값으로 저장
        cnt += 1  # 이건 리스트 인덱스 때문에 늘려주는 것

    elif sel == '2':
        idfalse = False  # 미리 false로 해둔 이유는 로그인 정보가 일치하지 않을 때의 값을 true로 두기 위해서
        loop = True  # 단순 while문을 돌리기 위한 변수
        while loop:
            userid = input("ID: ")
            pw = input("PW: ")
            for i in userList:  # 유저 리스트로 반복문을 굴리면서
                if i.userid == userid:  # 입력받은 아이디와 같은 아이디가 리스트 내에 있는지 확인하고
                    idfalse = False  # 얘는 계속 아이디가 틀린 게 아닌 이상 늘 false여야 하기 때문에 재차 초기화 해주는거고
                    if i.pw == pw:  # 여기서 비번까지 맞다면
                        print("로그인에 성공하였습니다.")  # 성공 메세지 띄우고
                        main()  # 메인화면 함수를 불러오는 것
                        loop = False  # while문을 종료시켜야 하기 때문에 false로 바꿔주고
                        break  # 해당 for문 또한 종료
                    else:  # 이건 아이디는 있는데 비번이 잘못됐을 경우
                        print("비밀번호가 잘못 입력되었습니다.")
                else:  # 이건 아이디가 등록되어 있지 않은 경우, 틀린 경우도 포함이겠죠
                    idfalse = True

            if idfalse:  # 여기서 아이디가 있는지 없는지 확인하고 없다면
                print("존재하지 않는 아이디입니다.")  # 존재하지 않는다고 알려주기

    """
    for i in userList:  # 이건 그냥 단순히 디버깅 용도로 회원 리스트 출력해주는 것
        print("{0}".format(i.printinfo()))
    """
