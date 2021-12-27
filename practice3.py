sentence = '나는 소년입니다'    # 문자열은 ' ', " " 모두 사용 가능
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """          
나는 소년이고
파이썬은 쉬워요.
"""                         # 여러 문장으로 된 스트링 정의
print(sentence3)


jumin ="990120-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2])
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6]) 

print("생년월일 : " + jumin[:6])
print("뒤 7자리 : " + jumin[7:])
print("뒤 7가지 : " + jumin[-7:])

print("나는 %d살입니다." %20)
print("나는 %s을 좋아해요" %"빨간색")

menu = ("돈까스","치즈까스")
print(menu)
print(menu[0])
print(menu[1])