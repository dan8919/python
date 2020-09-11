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

#값이 다르게 나옴 영상:31분

n,k = map(int,input().split())

result = 0
while True:
    # n k로 나누어 떨어지는 수가 될 때가지만 1씩 빼기
    target = (n//k) * k #몇개의 k의 배수가 나오고 차지하는 분량
    result += n-target  #1을 몇번 감해주는지 계산


#n k보다 작을 때 (더 이상 나눌 수가 없을 때) 반복문 탈출
    if n<k:
        break
    #k로 나누기
    result += 1
    n//=k

#마지막 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)
