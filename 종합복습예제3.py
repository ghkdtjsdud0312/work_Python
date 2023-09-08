# 3번 문제 : 대소문자 바꾸기
# 영어 소문자와 대문자로 이루어진 단어를 입력 받은 뒤, 대문자는 소문자로, 소문자는 대문자로 바꾸어 출력하는 프로그램을 작성하시오.
import IPython.extensions.autoreload

rst = "" # 공백 만들어 줘야 에러가 안남 / 외부에서 미리 만들어놓고 집어넣어야 해서 공백으로 만들어둠
for e in input() : # 입력 받는 문자열 만큼 자동 순회
    if e.islower():
        rst += e.upper() # 공백에 문자욜 추가되서 대문자로 만들어 줌
    else:
        rst += e.lower()
print(rst)