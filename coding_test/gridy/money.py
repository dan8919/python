#문제1:
#거스름돈 N원을 줘야 하는데 동전의 최소 개수를 구하기
#(500원, 100원, 50원, 10원)

n = 12340
count = 0
array = [500,100,50,10]

for coin in array:
    count += n//coin
    n %= coin  # n = n%coin
    print("count",coin,":",count)


print("count_total:",count)