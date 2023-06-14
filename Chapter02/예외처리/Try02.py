def division():
    try:
        num1= int(input("첫번째 정수를 입력해주세요>"))
        num2= int(input("두번째 정수를 입력해주세요>"))
        result = num1 / num2
    except ValueError:
        print("숫자로 된 정수를 입력해 바보야 !")
    except ZeroDivisionError:
        print("나누기에 0을 넣으면 멍청이 ~")
    except Exception as e: #as 는 뒤에 변수를 앞 메서드 별명으로 붙여줌
        print(e)
    else : #return 값을 else구문으로 뺌
        print("정상적으로 나누기 함수가 호출되었습니다 !")
        return print("{}을 {}로 나눈값은 {}입니다.".format(num1, num2,result))

division()