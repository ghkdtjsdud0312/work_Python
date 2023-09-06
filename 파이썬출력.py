# 파이썬의 다양한 출력 방법
name = "곰돌이사육사"
age = 20
gender = "남성"
jobs = "소프트웨어 개발자"
addr = "서울시 강남구 역삼동"

# C언어 스타일 : 서식지정자를 사용하는 방식
print("=" * 5, "C 스타일", "=" * 5)
print("이름 : %s" % (name)) # 괄호 생략 가능/ 붙여서도 가능
print("나이 : %d" % (age))
print("성별 : %s" % (gender))
print("직업 : %s" % (jobs))
print("주소 : %s" % (addr))

# 파이썬 스타일 : 3.6 이전 방법
print("=" * 5, "파이썬 스타일", "=" * 5)
print("이름과 주소 : {} / {}".format(name,addr))
print("나이 : {}".format(age))
print("성별 : {}".format(gender))
print("직업 : {}".format(jobs))

# 파이썬 현재 스타일 : 3.6 이후 방식, f와 {} 사용 해서 출력 하는 방식
print("=" * 5, "파이썬 현재 스타일", "=" * 5)
print(f"이름 : {name}")
print(f"나이 : {age}, 성별 : {gender}, 직업 : {jobs}")
print(f"주소 : {addr}")

# 자바 스타일
print("=" * 5, "자바 스타일", "=" * 5)
print("이름 : " +name)
print("나이 : " +str(age)) # 형변환
print("성별 : " +gender)
print("직업 : " +jobs)
print("주소 : " +addr)

# 출력 시 정렬
# < 좌측 정렬
# > 우측 정렬, 생략 가능
# ^ 중앙 정렬
print("|{:>5}|".format(10)) # 총 5칸을 잡고 우측 정렬
print("|{:<5}|".format(10))
print("|{:^6}|".format(10))

num = 10
print(f"|{num:>5}|") # 10이라는 값을 : 5칸 포함에 우측 정렬
print(f"|{num:<5}|")
print(f"|{num:^5}|")

PI = 3.14159265
print(f"{PI:.2f}") # .2f 소수점 이하 두 자리만 찍는다.
print(f"{PI:}")
print(f"{PI:.4f}")




