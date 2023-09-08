# 외장 함수 : 파이썬이 기본적으로 제공, import가 필요함
import random
# randint(0, 4) : 0에서 4 이하의 임의의 정수값이 반환
# randrange(0, 4) : 0에서 4 미만의 임의의 정수값이 반환
import random

for i in range(100) : # 4가 포함됨
    rand = random.randint(0, 4)
    print(rand)

for i in range(100): # 4가 포함안됨
    rand = random.randrange(0, 4)
    print(rand)

# 현재 시간 가져오기
# import datetime -> datetime.datetime.today() # datetime 두번

from datetime import datetime # datetime 모듈에서 datetime 함수만 import 함

print(datetime.today()) # datetime 1번 / 현재 날짜 가져 오기
print(datetime.today().year) # 현재 연도 가져 오기
print(datetime.today().month)
print(datetime.today().day)
print(datetime.today().hour)
print(datetime.today().minute)
print(datetime.today().second)

# 수학 계산을 위한 math
import math
print(math.sin(100)) # 사인값
print(math.cos(100)) # 코사인
print(math.tan(100)) # 탄젠트
print(math.log(100)) # 로그값
print(math.ceil(100.1)) # 무조건 올림
print(math.floor(100.9999)) # 무조건 내림

# pip = package import python
# pip install simple-colors 추가
