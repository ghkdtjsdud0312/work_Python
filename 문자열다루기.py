# 인덱싱과 슬라이싱

# jumin = "901120-1234567"
#
# gender = jumin[7]   #성별
# year = jumin[:2]   #출생년도
# month = jumin[2:4]   #월, 2번 인덱스 이상 4번 인덱스 미만
# day = jumin[4:6]   #일
#
# print("생년월일 : " + jumin[:6])
# print("뒤 7자리 : " + jumin[7:])
# print("뒤 7자리 : " + jumin[-7:])   #맨 뒤자리가 -1
#
# if gender == "1" :
#     print("남성입니다.")
# else:
#     print("여성입니다.")
#
# a = "Life is too short, You need Python"
# b = a[0] + a[1] + a[2] + a[3]
# print(b)
# a[1] = "L"   #문자열의 요소는 읽을 수는 있지만 변경은 되지 않음. 리터럴 상수

# 대소문자 바꾸기
aa = "Hello Python Program...."
bb = aa.upper()
print(bb)
print(aa.lower())

# 자바에서는 replace 일반문자
# replaceAll정규식

# 문자열 변경 : replace("")
input_str = "Hello Python Program...."
new_str = input_str.replace("Python","JavaScript")
print(new_str)

input_str = "Hello Python Program...."
new_str = input_str.replace("Python","")
print(new_str)

# 문자열에 포함된 문자 갯수 세기, 길이 확인
input_str2 = "Hello Python Program"
print(input_str2.count("lo"))   #문자열에서 포함된 문자(열)의 갯수를 반환
print(len(input_str2))   # 문자열의 길이를 반환, 별도의 외부 함수를 사용 하는 방식

test = [1,2,3,4,5,6,7,8,9,10]
print(f"길이{len(test)}")

print(input_str2.__len__())   #문자열에 포함된 내장 함수

# 문자열 찾기 : find() - 순방향, rfind() - 역방향, index()
# find() : 찾은 문자열의 첫 번째 인덱스를 반환, 못 찾으면 -1을 반환
# index() : 찾은 문자열의 첫 번째 인덱스를 반환, 못 찾으면 ValueError 예외 발생

# phrase = "가장 큰 실수는 포기, 가장 어리석은 일은 남의 결정 찾기, 가장 좋은 선물은 용서"
# print(phrase.find("가장"))   # 앞에서 부터(0번째)
# print(phrase.rfind("가장"))   # 뒤에서 부터 찾지만 위치에 대한 인덱스는 앞에서 부터 계산(34번째)
# print(phrase.index("포기"))
#
# print(phrase.find("나에게"))   # 못 찾으면 -1
# print(phrase.index("나에게"))   # 해당 하는 문자열이 없으면 오류 뜸/ 못 찾으면 value error
#
# new_pharase = phrase.replace("가장", "나에게")
# print(new_pharase)

# 문자열 연산
print("태양고" + "나희도")   # 가능
# print("태양고" + 2)   # 문자열과 정수의 연산 불가능
print("안녕하세요"*3)   # 해당 문자열을 수만큼 반복 수행
print("안녕하세요", "!"*5, "\n","\t","="*3, "태양고", "="*3, "\n나희도"*3,"입니다.")

# 문자열 앞/뒤 공백 제거 : strip()
input_aa = """
    안녕하세요.
문자열 함수를 알아 봅시다.


"""
print(input_aa.strip())


