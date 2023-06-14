str_slice = "0123456789"

print(str_slice[0:6]) #마지막 숫자는 포함되지 않음으로 012345 출력
print(str_slice[0:]) #마지막 숫자까지 포함되어 출력
print(str_slice[:10]) #처음 숫자 포함되어 출력
print(str_slice[1:3])
print(str_slice[:])#처음부터 마지막까지 출력
#-1이 9지만, 마지막숫자는 포함되지 않음으로 2345678 출력
print(str_slice[-8:-1])

#Step : 마지막에 붙여주는 숫자는 몇개씩 갖고올건지를 설정하는 것
str_step = "01234567"
print(str_step[0:10:2])
print(type(str_step[0:10:2]))

print(str_step[1:4:3])

#제일 끝에서부터 3개씩 갖다주세요
print(str_step[::-3])
print(str_step[8::-3])
print(str_step[-1::-3])

str_python = "Python"
print(str_python[0:]+str_python[::-1])
print(str_python[0]+str_python[-5:-2]+str_python[4:])

