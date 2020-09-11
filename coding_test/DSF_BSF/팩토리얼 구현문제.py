#n! = 1*2*3*4*....*(n-1)*n
#0! 과1! 의 값은 1입니다
#recursive로 해결

result = 1
def no_recursive(n):
    global result  #전역변수를 지역 범위(local scop)e에서 사용하고 싶다면

    for i in range(1,n+1):
        result = result*i
    return result

print(no_recursive(5))


def recursive(n):
    if n<=1:
        return 1
    return n * recursive(n-1)

print(recursive(0))

