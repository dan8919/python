# 문제2:
# N가 1이 될 때까지 다음의 두 과정중 하나를 반복
# 1.N에서 1을 뺍니다
# 2.N 을k 로 나눕니다.
#
# 예:N 17 K 4
# 17-1=16
# 16/4 =4
# 4/4 =1
# total 3번

n,k = map(int,input().split())

count = 0

while n>1:
    if n%k == 0:
        n = n//k
        count +=1
    elif n%k != 0:
        n= n-1
        count += 1

print("count:",count)
