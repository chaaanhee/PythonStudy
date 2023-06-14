# SyntaxError == 구문오류
# EOL == End Of Line 문장 끝에 오류발생
# IndentationError == 들여쓰기 에러
# TabError == 들여쓰기와 스페이스를 섞어서 사용했을때 발생하는 에러
# 순차적으로 에러발생이 아닌, 오류가 있으면 출력이 안돼
# KeyboardInterrupt == control + c 를 누르면 발생하는 에러
# !try 들여쓰기 주의!
def division():
    try:
        num1= int(input("첫번째 정수를 입력해주세요>"))
        num2= int(input("두번째 정수를 입력해주세요>"))
        return print(f"{num1}을 {num2}로 나눈 값은 {num1 / num2}입니다.")
    except ValueError:
        print("숫자로 된 정수를 입력해 바보야 !")
    except ZeroDivisionError:
        print("나누기에 0을 넣으면 멍청이 ~")
    except Exception as e: #as 는 뒤에 변수를 앞 메서드 별명으로 붙여줌
        print(e)
    finally : #예외발생에 관계없이 무조건 실행되는 구간 / return 값이 있으면 바로 함수를 빠져나오기때문에, else는 안돼
        print("정상적으로 나누기 함수가 호출되었습니다 !")

division()

#ValueError, ZeroDivisionError, KeyboardInterrupt
#help(ZeroDivisionError) 인자에 대한 도움말을 나타내주는 메서드
