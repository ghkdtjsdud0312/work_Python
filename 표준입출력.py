print(39) # 정수형
print("문자열")  # 문자열
print([1, 2, 3])  # 리스트형
print(1+3)
print("파"+"이"+"썬")  #문자열 이어붙이기
print("파""이""썬")
print("파","이","썬")  #콤마를 구분자(세퍼레이트)라고 부른다. 기본적으로 한칸의 공백을 가지고 있음
print("파\n\n\n이\t\t썬")  #\n은 줄바꿈 \t는 탭(4칸 띄기)
print("""동해물과 백두산이 마르고 닳도록 하느님이
보우하사 우리나라 만세
무궁화 삼천리 화려 강산
대한 사람 대한으로 길이 보전 하세
""")
print("안녕하세요 라고 \"곰돌이사육사\"가 말했습니다.")  # \" \" 은 강조 표시


# end와 sep 옵션
# end : 출력문에서 끝에 자동으로 삽입되는 문자를 지정하는 옵션 : \n
# sep : 출력문의 중간에 삽입되는 문자를 지정하는 옵션 : 기본은 space

print("Hello", end="$")  # end=" " 줄바꿈 되지 않음 / 원래 한칸 공백이 기본적으로 있음
print("Hello", end="*")  #println 같은 효과가 있음 -> end="\n"
print("Hello")  #end="$" -> 공백에 채워짐

print("life", "is", "too", "short", sep="/") # 자동으로 한칸 공백 줌
print("life", "is", "too", "short", sep="\n")
print("life", "is", "too", "short", sep="\\") # \\은 특수문자라 2개써야함

print("010","1234","5678", sep="-")

year = 2023
month = 9
day = 6
print(year, month, day, sep="/")