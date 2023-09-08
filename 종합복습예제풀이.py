# 회원 정보 출력 하기
def input_age() : # 함수를 부르는 단어
    while True:
        age = input("나이를 입력 하세요 : ")
        if age.isdigit():  # 문자열이 숫자로 구성되어 있는지 확인
            age = int(age)
            if 0 < age < 200: return age # 반환 타입값이 없음
        print("나이를 잘 못 입력 하셨습니다.")

def input_gender() :
    while True :
        gender = input("성별을 입력 하세요 : ")
        if gender == 'M' or gender == 'm' : return "남성"
        elif gender == 'F' or gender == 'f': return "여성"
        print("성별이 잘 못 되었습니다.")

def input_jobs() :
    while True :
        jobs = input("직업을 입력 하세요 : ")
        if jobs.isdigit():
            jobs = int(jobs)
            if 0 < jobs < 5: return jobs
        print("직업을 잘 못 입력하셨습니다.")

def print_info(name, age, gender, jobs) :
    jobs_str = "", "학생", "회사원", "주부", "무직"
    print("=" * 3, "회원정보", "=" * 3)
    return f"이름 : {name}\n나이 : {age}\n성별 : {gender}\n직업 : {jobs_str[jobs]}"
    # print(f"""이름 : {name}\n나이 : {age}\n성별 : {gender}\n직업 : {jobs_str[jobs]}""")

#함수는 선언 이후 호출해야 동작 함
member_info = "member.txt"
fd = open(member_info, "wt", encoding="utf-8")
while True:
    name = input("이름을 입력하세요 (종료하려면 quit) : ")
    if name == 'quit' : break
    age = input_age()
    gender = input_gender()
    jobs = input_jobs()
    rst = print_info(name, age, gender, jobs)
    fd.write(rst + "\n")
fd.close()
#--------------------------------------------------------------

# name = input("이름을 입력 하세요 : ")
# while True :
#     age = input("나이를 입력 하세요 : ")
#     if age.isdigit() : # 문자열이 숫자로 구성되어 있는지 확인
#         age = int(age)
#         if 0 < age < 200 : break
#     print("나이를 잘 못 입력 하셨습니다.")
#
# while True :
#     gender = input("성별을 입력 하세요 : ")
#     if gender == 'M' or gender == 'm' or gender == 'F' or gender == 'f': break
#     print("성별이 잘 못 되었습니다.")
#
# while True :
#     jobs = input("직업을 입력 하세요 : ")
#     if jobs.isdigit() :
#         jobs = int(jobs)
#         if 0 < jobs < 5 : break
#     print("직업을 잘 못 입력 하셨습니다.")
#
# if gender == 'M' or gender == 'm' : gen_str = "남성"
# else: gen_str = "여성"
#
# jobs_str = "", "학생", "회사원", "주부", "무직" # 안 써도 튜풀가능(튜플) / 임의로 만들어진 데이터를 여러군데 나눠 담는 것
# print("="*3, "회원정보", "="*3)
# print(f"""이름 : {name}
# 나이 : {age}
# 성별 : {gen_str}
# 직업 : {jobs_str[jobs]}
# """)