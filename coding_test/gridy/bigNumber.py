
#숫자를 입력하고 숫자들로 계산하여 제일큰 숫자를 만들기

data = input()  #input 이 리스트로 됨


result = int(data[0])

for i in range(1,len(data)):
    num = int(data[i])
    if num<=1 or result <= 1:
        result += num
    else:
        result *= num


print(result)