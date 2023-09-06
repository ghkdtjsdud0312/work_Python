# 값을 할당하는 방법
# a = b = c = 1
# print(a, b, c)
#
# a, b, c = 1, False, "곰돌이사육사"  #여러 개의 변수를 한번에 대입
# print(a, b, c)
#
# # 타입 확인
# age = int(input("나이를 입력 하세요 : "))
# print(type(age))

# value = 0o77  # 8진수 결과 63
# print(value)
#
# value = 0xff  # 16진수 결과 255
# print(value)
#
# value = 0xffffff  # 16진수 결과 16777215(컬러값 흰색)
# print(value)
#
# value = 0xff0000  # 16진수 결과 16711680(빨간색)
# print(value)
#
# # 블리언 타입 : 참과 거짓의 값을 확인
# print(bool(1))   # True
# print(bool(0))   # False
# print(bool(-1000))   # True
# print(bool(""))   # False
# print(bool(None))   # False(값이 정해지지 않았음을 의미)
#
# # 문자열 타입 :
# str1 = "Hello Python!!!"
# print(str)
# print(str[0])   # 인덱싱
# print(str[2:5])   #2번 인덱스이상 5번 인덱스 미만까지 llo
# print(str[2:])   # 2번 인덱스에서 끝까지
# print(str * 3)
# print(str + "TEST")

# 형변환 : 파이썬은 값이 할당되는 순간 형이 결정됨, 이후 데이터형을 변경하고자 할 때 형 변환을 사용
print(10 + int("10"))
print("나이 : " + str(30))
print(1 + 3.141592 + float("4.44"))

