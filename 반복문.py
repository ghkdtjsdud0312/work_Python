 # 반복문 : 조건이 참인 동안 계속 수행되는 구문

n= int(input("정수를 입력 하세요 :"))
sum = 0
while n : # 파이썬은 정수값이 0이 아니면 참으로 간주함
    sum += n
    n -= 1 # 파이썬은 증감 연산자가 없음, 복합대입연산자 써야 함
print(sum)

while True:
    age = int(input("나이를 입력 하세요 : "))
    if 0 < age < 200: break
    print("나이 입력 범위가 벗어 났습니다.")


# for 요소 in 시퀀스 : 시퀀스의 각 요소를 순회하는데 사용(자바의 향상된 for문과 동일)

fruits = ["apple","banana","cherry",["seoul","korea"]]
print(fruits[3][1][0]) # 3번째 인덱스에 1번쨰 인덱스에 첫번쨰글자 -> k
for e in fruits :
    print(e[0])

str1 = "서울시 강남구 역삼동 KH정보교육원"
for e in str1 :
    print(e,end="/")

# for 변수 in range(시작값, 종료값, 증감값)

n = int(input("정수를 입력 하세요 : "))
sum = 0
for i in range(1, n+1): # 1부터 n+1미만
    sum += i
print(sum)

# # for문을 역순으로 반복하기
for i in range(10, -1,-2): # 10 ~ 0까지 출력
    print(i)

# 이중 for문
n = int(input("정수를 입력 하세요 :"))
for i in range(0, n):
    for j in range(0,n):
        print("*",end ='0')
    print()

for i in range(2, 10): #2단~9단
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}")
    print()

# # 홀수/짝수 나누어 찍기
n = int(input("정수 입력 :"))
for i in range(0,n):
    for j in range(0,n):
        if j %2 == 0 : print("$", end=' ')
        else: print("*", end=' ')
    print()

# 사각형 찍기
# 정수값을 n을 입력 받아 n*n 크기의 행렬을 출력하는 프료그램 작성
# 값은 1부터 시작, 이쁘게 찍기
# 4
# 1  2  3  4
# 5  6  7  8
# 9 10 11 12
#13 14 15 16
n = int(input("정수 입력 : "))
for i in range(1,n * n+1):
    print(f"{i:3}",end='') # i:>3
    if i % n == 0 : print()

# 별찍기
#*
#* *
#* * *
#* * * *
#* * * * *
n = int(input("별 개수 찍기 : "))
for i in range(n) :
    for j in range(i+1):
        print("*", end=" ")
    print()


#* * * * *
#* * * *
#* * *
#* *
#*
n = int(input("뒤집어진 역직각삼각형 : "))
for i in range(n):
    for j in range(n-i):
        print("*", end=" ")
    print()


#* * * * *
# * * * *
#  * * *
#   * *
#    *
n = int(input("역삼각형 : "))
for i in range(n):
    for k in range(i): print("", end=" ")
    for j in range(n-i):print("*", end=" ")
    print()

n = int(input("역삼각형 : "))
for i in range(n, 0, -1):
    for s in range(n-i):
        print("", end=" ")
    for j in range(i):
        print("*", end=" ")


#* * * * *
#  * * * *
#    * * *
#      * *
#        *
n = int(input("뒤집어진 역직각삼각형(반대) : "))
for i in range(n):
    for k in range(i): print(" ", end=" ") # 공백을 먼저 뺴준다.
    for j in range(n - i): print("*", end=" ")
    print()

# 문자와 ASCII 코드
# chr : 유니코드(=ASCII 코드) 값을 입력 받아 그 코드에 해당하는 문자를 출력 /2바이트로 한글로 코딩 가능
# ord : 문자를 유니코드값으로 변환

for i in range(ord("A"),ord("Z")+1): # 65:A
    print(chr(i), end=" ") # chr 문자 출력
print()

for i in range(65,91):# A:65 Z:90
	print(chr(i), end=" ")
print()

