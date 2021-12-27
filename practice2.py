number = 2+3*4
print(number)
number = number +2
print(number)
number += 2
print(number)
number *= 2
print(number)
number /= 2
print(number)
number -= 2
print(number)

number %= 5
print(number)

print(abs(5))    # 절대값 연산자
print(pow(4,2))   # 승 연산자
print(max(5,12,17))  # 최대값 연산자
print(min(2,6,8,9,12)) # 최소값 연산자
print(round(3.14))  # 반올림 연산자
print(round(4.99))  # 반올림 연산자

from math import *

print(floor(4.99))  # 내림 연산자
print(ceil(3.24))  # 올림 연산자
print(sqrt(16)) # 제곱근 연산자

from random import *

print(random())  # random 함수 생성함수 : 0.0~1.0 사이의 값 생성
print(random()*10)   # random 함수 생성함수 : 0.0~10.0 사이의 값 생성
print(int(random()*10))  # random 함수 생성함수 : 0.0~10 사이의 정수값 생성
print(int(random()*10) + 1)  # random 함수 생성함수 : 1~10 사이의 정수값 생성
print(int(random()*45) + 1) # random 함수 생성함수 : 1~46 사이의 정수값 생성


print(randrange(1, 46)) # randrange : 입력 숫자의 영역내에서 난수발생 함수 ,1~46 이하의 난수 생성 함수 

date = int(random()*10) + 4
print(date)
date=(randrange(4,28))
print("오프라인 스터디 모임은 매월",date,"일로 선정되었습니다.")