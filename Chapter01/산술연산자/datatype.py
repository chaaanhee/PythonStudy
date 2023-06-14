#자료형 -> 다른 자료형으로 변환

##int() 정수형
#>>실수형, 논리형, 문자열
print(int(123.94e2))
print(int(123.942))

print(int(True)) #1로 변환
print(int(False)) #0로 변환

print(int("2435344"))
print(type(int("2435344")))
#print(int("123.ㄹㅇ")) 에러:정수 이외에 다른 문자가 들어가면 에러

##float() 실수형
#정수형, 논리형, 문자열
print(float(200))
print(float(3))

print(float(True)) #1로 변환 1.0
print(float(False)) #0로 변환 0.0

print(float("12.34567"))
print(float("1212"))

#str() 문자열
#모든 자료형
print(str(2435))
print(str(2435.123))
print(str(True))
print(str(False))
print(type(str(False)))

#bool() 불린형
#모든 자료형
#False : 0, 빈칸
print(bool(0))
print(bool(0.0))
print(bool(""))
#True : 1, 문자, 숫자 
print(bool(1))
print(bool(1.0))
print(bool("str"))
print(bool("1234"))
