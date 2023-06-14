a = 10
b = 20

#비교연산자 값은 bool형으로 결과값
print(a < b)
print(a <= b)
print(a > b)
print(a >= b)
print(a == b) #a와 b가 같을경우
print(a != b) #a와 b가 같지않을경우

#논리형자료(True:1 / False:0)
is_ture = True
is_false = False

print(is_ture > is_false)
print(is_false > is_ture)

#문자형 자료:소문자가 대문자보다 큰 값
print("Python" > "python") #False

#문자형 자료:더 큰 정수(+소수)를 가진 문자열이 더 큰 값 
print("12345" > "12344")
print("12.12" < "13.12")