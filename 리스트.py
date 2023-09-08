# 리스트 : 크기가 정해지지 않은 요소들에 대한 값을 저장하기 위한 자료형
# 특징 : 크기가 정해지지 않음 / 아무 자료형이나 와도 됨 / 중첩 사용이 가능 [[],[],[],[]]/[[]] 가능
# 뮤터블 객체(읽고 쓰기가 가능)

number = [1,2,3,4,5,6]
fruits = ["apple","banana","orange"]
mixed = [1, True, "seoul", 12.3444]
dup = [[1,2,3,4,5], ["apple", "키위"]]

# 변수와 리스트를 비교 해보기(개수 맞아야 함)
# kor, eng, mat = map(int,input("성적 입력 : ").split())
# print(sum([kor, eng, mat]))

# 리스트는 성적의 개수에 상관없이 입력 받을 수 있음
# score = list(map(int,input("성적 입력 : ").split()))
# print(sum(score)/len(score))


str_name = ["seoul", "gangnam", "suwon", "inchon"]
# 인덱싱
print(str_name) # 리스트 전체 출력
print(str_name[1]) # 1번째 요소 출력
print(str_name[1][2]) # 1번째 요소의 2번째 문자 출력

# 슬라이싱(잘라 내는 것)
slice = str_name[1:3] # 1번에서 3번미만까지 잘라냄
print(slice)
print(len(slice[0]))

primes = [2,3,5,7]
print(primes[0])
print(primes[-1]) # 뒤에서부터 읽음
print(primes[-2:])



