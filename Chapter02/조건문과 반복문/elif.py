#조건이 참과 거짓 이외에 더 많은 조건을 갖고있을 때 사용
lunch_menu = input("점심메뉴를 말씀해주세요.")
if lunch_menu == "pork": #무조건 앞엔 if 문이 있어야 함.
    print("eat pork")
elif lunch_menu == "beef":
    print("eat beef")
elif lunch_menu == "gimbab":
    print("eat gimbab")
else : 
    print("no eat")

#3의 배수이면서 짝수인 수를 판별해주는 조건식
number = int(input("숫자를 입력해주세요."))
#if number % 3 == 0 and number % 2 == 0: #or >> 3의 배수이거나, 짝수입니다.>>모두 거짓이여야 else 출력
#    print("3의 배수이면서 짝수입니다.")
#elif number % 3 != 0 :                 
#    print("3의 배수가 아닙니다")
#elif number % 2 != 0 :    
#    print("짝수가 아닙니다")
#else :
#    print("3의 배수 또는 짝수가 아닙니다.")

if number %3 == 0 or number %2 == 0 :
    if number %3 == 0 and number %2 != 0 :
        print("3의 배수입니다.")
    elif number % 3 == 0 and number %2 == 0:
        print("3의 배수이면서, 짝수입니다.") 
    else :
        print("짝수입니다.")
else : 
    print("3의 배수도, 짝수도 아닙니다.")

#웹사이트 주소를 입력해주세요 > 마지막 주소값으로 나라맞추기
website = input("웹사이트 주소를 입력해주세요")
#print(website.split(".")) 각 웹사이트의 주소가 다르기에 스플릿으로 먼저 나눠, 리스트로 출력
nation = website.split(".")
if nation[-1] == "kr" :
    print("한국")
elif nation[-1] == "uk" :
    print("영국")
elif nation[-1] == "com" : 
    print("기업용")
elif nation[-1] == "org" :
    print("기관") 
else :
    print("알 수 없음")           