# 1번 문제 : 회원 정보 출력 하기
# 1단계 : 현재 상태대로 -> 함수 형태로

name = input("이름을 입력하세요 : ")
while True:
    age = int(input("나이를 입력하세요 : "))
    if 0 < age < 200: break
    print("나이를 잘못 입력 하셨습니다. 다시 입력하세요.")

while True:
    gender = input("성별을 입력하세요 : ")
    if gender == "M" or gender == "m":
       gen_name = "남성"
       break
    elif gender == "F" or gender == "f":
         gen_name = "여성"
         break
    else: print("성별을 잘못 입력하셨습니다. 다시 입력하세요.")

while True:
    jobs_name = ("", "학생", "회사원", "주부", "무직")
    jobs = int(input("직업을 입력하세요 : "))
    if 0 < jobs < 5 : break
    print("직업이 잘못 입력되었습니다. 다시 입력하세요.")

# if gender == "M" or gender == "m":
#     gen_name = "남성"
# else:
#     gen_name = "여성"
#
# jobs_name = ("","학생","회사원","주부","무직")

print("="*3, "회원정보", "="*3)
print(f"이름 : {name}")
print(f"나이 : {age}")
print(f"성별 : {gen_name}")
print(f"직업 : {jobs_name[jobs]}")


# 2번 문제 : 핸드폰 요금 계산하기
n= int(input()) # 통화 개수
call = list(map(int, input().split())) # 통화 시간

y_pay = m_pay = 0
for i in range(n):
    y_pay += (call[i] // 30) * 10 + 10
    m_pay += (call[i] // 60) * 15 + 15

if y_pay > m_pay:
    print("M",m_pay)
elif y_pay < m_pay:
    print("y",y_pay)
else:
    print("Y M",y_pay)


# 3번 문제 : 대소문자 바꾸기
r= ""
for i in input():
    if i.islower():
        r += i.upper()
    else:
        r += i.lower()
print(r)


# 4번 문제 : 숫자의 개수

a,b,c = map(int, input("정수 3개 입력 : ").split())
ls = str(a*b*c)
for i in range(10):
    print(ls.count(str(i)))