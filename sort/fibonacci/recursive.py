#첫 둘째 항이 1이며 그 뒤의 모든 항은 바로 앞 두 항의 합
#10번쨰 항의
k = 10





def fib(n):
    if n<2:
        return 1
    return fib(n-1)+fib(n-2)

print(fib(k))



#피보나치 수열 배열
arr = []
for i in range(k+1):
     k = fib(i)
     arr.append(k)
print(arr)


