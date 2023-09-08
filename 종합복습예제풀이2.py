# 2번 문제 : 핸드폰 요금 계산하기
# 영식 요금제 : 30초에 10원
# 민식 요금제 : 60초에 15원

n=int(input()) # 통화 횟수
call = list(map(int, input().split())) # 통화 횟수에 대한 통화 시간 /list는 크기를 늘리는 것
# input을 받고 문자열로 받는다.
# split은 공백 한칸 기준으로 쪼개서 int 형으로 바꿈
# map은 입력 받은걸 앞에 원하는 타입으로 바꿈, 함수도 가능
# list는 받아 주는 애가 있어야 하는데 알수가 없으니 갯수가 정해 지지 않은 배열을 만들수 있어 쓴다.
y_pay = m_pay = 0
for i in range(n) :
    y_pay += (call[i] // 30) * 10 + 10
    m_pay += (call[i] // 60) * 15 + 15

if y_pay > m_pay:
    print("M",m_pay)
elif y_pay < m_pay:
    print("y",y_pay)
else:
    print("Y M",y_pay)