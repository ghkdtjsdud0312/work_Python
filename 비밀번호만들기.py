# 각 사이트 비밀번호 만들기
# 규칙 : http://naver.com 앞의 http:// 잘라내기
# 규칙 2 : 처음 만나는 점 이후 제거
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자에 포함된 'o'의 갯수 + 글자에 포함된 'k'의 갯수 + "!" + 자신의 이니셜

file_name = "password.txt" # 돌리면 적은 내용 파일 만들어짐
fd = open(file_name, "wt")

while True : # while문 들여쓰기해야 안에 들어가고 밖에 쓰면 나가짐
    url = input("사이트 : ")
    if url == "exit" : break # exit누르면 나가짐
    my_str = url.replace("http://","")
    my_str = my_str[:my_str.index(".")] # 슬라이싱 : 처음부터 "." 인덱스 미만 까지 / my_str.index(".")에 5가 들어옴
    password = my_str[:3] + str(len(my_str)) + str(my_str.count("o")) + str(my_str.count("k")) + "!" + "jks"
    #  my_str[:3]는 nav
    print("비밀번호 : " + password)
    fd.write(password + "\n")
fd.close()
