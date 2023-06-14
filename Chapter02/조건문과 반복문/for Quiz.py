#메뉴 딕셔너리를 갖고 결과 출력
#차가운 메뉴
#제품명 : 아이스 아메리카노, 가격 3000
#..
#뜨거운 메뉴
#제품명 : 아메리카노, 가격 2500
#...
menu = { "아이스 아메리카노":3000, "아메리카노":2500, "아이스 라떼":4000, \
 "라떼":3500, "아이스크림":8000 }
ice_menu = {}
hot_menu = {}

for i, j in menu.items():
    if i[0:3] == "아이스":
        ice_menu[i] = j
    else :
        hot_menu[i] = j

print("차가운메뉴")
for i,j in ice_menu.items():
    print("제품명 : {}, 가격 : {}".format(i, j))
print("뜨거운메뉴")
for i,j in hot_menu.items():
    print("제품명 : {}, 가격 : {}".format(i,j))