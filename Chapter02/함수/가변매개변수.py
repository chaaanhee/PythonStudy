
def add(num1, num2 = 40):
    return num1 + num2
print(add(10))

#기본 매개변수는 일반매개변수보다 앞에 있을 수 없다. 반드시 뒷 매개변수에 지정해야함.
''' 에러발생
def add(num1 = 10, num2):
    return num1 + num2

print(add(10))
'''
def add3(num1, num2=30, num3=10):
    return num1 + num2 + num3
print(add3(num1=20, num3 = 2)) #함수안에 기본매개변수를 셋팅해도 호출할때 매개변수가 우선순위가 큼

a, b = 30, 10
def add2(num1 = a, num2 = b):
    return num1 + num2

a, b = 3, 5 #함수가 정의되는 시점에서 에볼루션(변수에 대한 평가)을 하기 때문에, 이 후 변수값이 바뀐다고 해도 출력되지 않음.
print(add2())
print(add2(a,b)) #바뀐값으로 출력

#가변매개변수 : 가변적으로 매개변수에 입력할 수 있는 것
#*을 붙이면 가변매개변수 : 여러개의 인자값을 받을 수 있다.
#보통 가변매개변수는 args(아규먼트의 약자)를 사용하는것을 권장
# 일반 매개변수 앞으로는 올 수 없음 (*args, num) = X // (num, *args) = O
# 가변매개변수를 인자로 받아서 return해보면 튜플로 반환
def add5(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)
add5(10, 20, 30, 40)

# 가변매개변수를 인자로 받아서 return해보면 튜플로 반환
def add7(*args):
    return args
print(add7(10, 20, 30))

