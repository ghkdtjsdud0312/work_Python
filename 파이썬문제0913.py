# 1. 배수 찾기(초급에 있음)
# 첫째 줄에 n이 주어짐, 다음 줄부터 값이 주어짐
# 목록에 있는 수가 n의 배수 인지 아닌지 판별
# 0을 입력 하면 목록이 끝남
# 3
# 1
# 7
# 99
# 321
# 777
# 0
# 1 is NOT a multiple of 3.
# 7 is NOT a multiple of 3.
# 99 is a multiple of 3.
# 321 is a multiple of 3.
# 777 is a multiple of 3.
# n = int(input()) # 문자열로 반환되기 때문에 정수타입으로 반환/1개만 받아서 list, map 필요 없음
# ls = [] # 결과를 한번에 찍어야해서 빈 리스트 생성
# while True: # 0이 입력 되기 전까지 반복 수행
#     x = (int(input())) # 목록의 수를 입력 받음
#     if x == 0: break # 0이 입력되면 탈출
#     ls.append(x)
#
# for e in ls: # 출력하는 값 입력
#     if e % n == 0: print(f"{e} is a multiple of {n}.")
#     else: print(f"{e} is NOT a multiple of {n}.")



# 2. 피타고라스 정리(중급에 있음)
# 피타고라스의 정리 : 직각삼각형에서 빗변을 제외한 나머지 두 변의 길이를
# 각각 제곱해 더하면 빗변의 길이의 제곱과 같다.
# 과거 이집트인들은 각 변들의 길이가 3, 4, 5인 삼각형이 직각삼각형인 것을 알아냈다.
# 주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.
# 6 8 10
# 10 8 6
# 25 52 60
# 5 12 13
# 0 0 0
# right
# right
# wrong
# right

rst =[] # 결과를 출력하기 위한 빈 리스트
while True:
    li = list(map(int,input().split()))
    li.sort()
    if li[0] == 0 and li[1] == 0 and li[2] == 0: break
    elif li[2] ** 2 == li[1] ** 2 + li[0] ** 2:
        rst.append("right")
    else:
        rst.append("wrong")

for e in rst: print(e)
