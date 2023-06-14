#파이썬의 내장함수
#print() 문자열로 출력
#input() 입력을 문자열로 반환

#사용자정의함수 -> 정의(define) 
#def 함수이름(): 괄호를 붙이는 것은 함수를 호출하는 것
#    수행할 코드

def menu():
    print("오늘의 메뉴")
    print("오늘 점심메뉴는 제육볶음입니다.")
    print("내일의 메뉴")
    print("내일 점심메뉴는 돈까스입니다.")
menu() #()로 함수를 호출

#내장함수는 ()안에 데이터를 입력, 함수를 만들때 매개변수를 추가, 함수를 호출할 때 인자를 넣는다.
#int등 리턴값이 없어도 숫자도, 문자도 모두 가능
def add(num1, num2): #매개변수, 파라미터
    ''' 간단한 메모
        편리하게 사용
    '''
    print(num1 + num2)
add(4,6)
print(add(4,7)) 
'''
none : 값이 없음. 
반환값이 없는 값이다.
print에서 나옴 값
'''

def myname(text1, text2) :
    text = text1 + text2 #전달받음 데이터들이 합쳐짐
    return text #함수호출지점으로 반환한다.
print(myname("김","찬희"))

#끝말잇기 함수 만들기
'''
def game(text):
    print(text)
    input("끝말을 이어주세요 >")
    for i,j in text():
        if i[0] == j[-1]:
            return text
        else :
            print("끝말이 이어지지 않습니다.")    
print(game("차표"))
'''
def game(text):
    while True:
        print(text)
        keyword = input("끝말을 이어주세요 >")
        if text[-1] == keyword[0]:
            text = keyword #텍스트에는 키워드라는 값을 할당해줘야함.
        else :
            print("끝말이 이어지지 않습니다.")
            break
game("차표")