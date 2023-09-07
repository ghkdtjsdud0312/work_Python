# 제어문이란? 조건문과 반복문을 의미하며 순차적인 흐름을 제어하는 목적으로 사용

# n = int(input("정수를 입력 하세요 : "))
# if n > 100:
#     print(f"{n}은 100보다 커요.")
# elif n < 100: # 다시 되물어보는 경우
#     print(f"{n}은 100보다 작아요.")
# else:
#     print("100과 같아요.")  # 뭐라도 넣어 주어야 함/ print()값이나 pass 넣어야 함

# 조건문에서 문자열 비교

while True:
    season = input("현재 계절을 입력 하세요 : ")
    if season == "spring": # 파이썬은 switch문이 없어 if문 사용
        print("봄이 왔어요.")
        break
    elif season == "summer":
        print("무더운 여름 입니다.")
        break
    elif season == "fall" or season == "autumn":
        print("가을이 왔어요.")
        break
    elif season == "winter":
        print("추운 겨울 입니다.")
        break
    else:
        print("계절을 잘못 입력하셨습니다.") # pass



