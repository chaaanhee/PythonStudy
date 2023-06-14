#키워드 반환값 = 특정값 형태로 {"키워드" : "특정값"}
#키워드 매개변수(**kwargs)
def star_player(**kwargs):
    for i in kwargs.items():
        print(i)
star_player(축구 = "손흥민", 야구 = "류현진", 농구 = "서장훈")

def soccer_player(**kwargs):
    for i, j in kwargs.items():
        if "박지성" in kwargs.values():
            print("전 박지성을 좋아했어요.")
        else :
            print("{}는 역시 {}!".format(i, j))
soccer_player(축구 = "손흥민")

#end 값은 키워드 매개변수
print(1,2,3,4, end = "@@@")

#일반매개, 가변매개(튜플로 반환), 기본 매개변수, 키워드매개변수(딕셔너리 형태로 반환)
# 위 순서가 매우 중요 !
def func_a(name, *args, address = "한국", **kwargs):
    print(name, args, address, kwargs)

func_a("홍길동", "옛날", "사람", address="한양", 직업 = "도둑")

#Quiz  최대값과 최소값 찾기

def max_min_search(*number):
    max_num = number[0]
    min_num = number[0]
    for i in number:
        if i > max_num :
            max_num = i
        elif i < min_num:
            min_num = i
    return max_num, min_num
            
print(max_min_search(15, 30, 4, 60, 7, 80, 32)) 

#max,min은 내장함수가 있다.
def max_min_search(*number):
    return max(number), min(number)

print(max_min_search(15, 30, 4, 60, 7, 80, 32)) 
