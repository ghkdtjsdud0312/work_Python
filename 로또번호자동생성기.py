# 중복 값이 없는 로또 번호 생성하기
import random
print("로또 번호 자동 생성기")
ls = [] # 빈 리스트 만들기 / []은 빈 리스트를 만드는 문법
while True :
    rand = random.randrange(1,46)
    if rand not in ls: # rand 값이 ls에 포함되어 있지 않으면 / list에 생성된 rand값이 포함되어 있지 않으면
        ls.append(rand) # add와 같은 뜻
    if len(ls) == 6: break
print(ls)

