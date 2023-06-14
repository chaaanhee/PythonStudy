#문자와 문자열 모두 string
text = "String Data Type"
text_02 = 'String "Date" Type'
print(text_02)

#탈출문자
# \는 긴 코드일때 가독성을 위한 코드, 하나는 표시되지 않음
# \', \", \\, \n, \r, \t
text_03 = "Python \'is\" Easy"
text_04 = "java Python \ris Easy" 
# 캐리지 리턴:\r 앞에있는 문자를 \r뒤에 있는 문자에 덮어씌운다.
text_05 = "Py\tthon is Easy" 
# tab문자:다음 8번째 위치로 이동,위에는 6번째, 8번째 이후에 쓰게되면 16번째 위치로 이동
print(text_03)
print(text_04)
print("text_05" + text_05)

#'''를 3개 사용하게되면 코드가 필요없이 그대로 출력
text_06 = '''Python
is
Easy'''
print(text_06)

#문자열 연산
text_07 = "Python is Easy"
text_08 = "and Powerful"
print(text_07 + text_08)
print(3 * text_07)
