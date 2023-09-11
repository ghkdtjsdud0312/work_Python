# 평균은 넘겠지?
def over_rate() :
    ls = list(map(int,input().split()))
    average = sum(ls[1:])/len(ls[1:])
    cnt = 0
    for i in range(1,len(ls)) :
        if ls[i] > average: cnt+=1


