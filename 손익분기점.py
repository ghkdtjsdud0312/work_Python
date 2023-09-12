# 손익분기점 : 매출액 = 고정비/(1-변동비/매출액) = 고정비/공헌이익률
# 고정비용 : 1000
# 가변비용 : 70
# 판매비용 : 170

# fix, var, sell = map(int,input().split())
# cnt = 0
# while True :
#     # if fix + (var * cnt) < sell * cnt : break
#     if cnt > fix // (sell - var) : break
#     cnt += 1
#
# print(cnt)

fix, var, sell = map(int,input().split())
if sell <= var: print(-1)
else: print(fix // (sell-var) + 1)