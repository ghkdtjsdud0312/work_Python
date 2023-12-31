# import math # math 모듈을 사용하기 위해서 import 함
# print(math.sin(1))

# 모듈 내에 특정 함수(메서드)만 가져오고자 하는 경우
# from math import sin, cos, tan
# print(sin(1))
# print(cos(1))
# print(tan(1))

# 모듈을 가져올 때 충돌이나 긴 이름을 간결하게 사용하기 위해 별칭 부여(별칭을 부여하면 원래 이름은 사용 안됨)
# import math as m
# print(m.sin(1))
# print(m.cos(1))
# print(m.tan(1))

# sys 모듈 : 시스템과 관련된 정보를 가지고 있는 모듈
# import sys
# print("명령줄 인수 : ", sys.argv) # 명령줄 인수 출력
# print("실행 경로 : ", sys.path[0]) # 스크립트 실행 경로
# sys.stdout.write("Hello, world !!!\n") # 표준 출력
# sys.stderr.write("Error !!!\n") # 표준 에러 출력
# sys.exit(0) # 프로그램 강제 종료

# os 모듈 : 운영체제와 상호 작용하기 위한 기능을 제공(파일 시스템 접근, 환경 변수 제어, 프로세스 관리 등)
import os
cwd = os.getcwd() # 현재 작업 디렉토리
print("현재 작업 디렉토리 : ", cwd)
# 디렉토리 생성
is_dir = os.path.isdir("testdir")
if not is_dir: os.mkdir("testDir") # 디렉토리 생성
is_file = os.path.isfile("score.txt")
print(is_file)

os.system("dir")
