# 두 수를 받아,사칙연산(+,-,*,/)을 수행하는 함수를 만들어 보시오.
# $>3+4 answer is 7

# $>234*234 answer is 7
#주석
#함수 하나당 함수 5줄 넘지 말자

def plus(a, b):
    return a + b
def minus(a, b):
    return a - b
def multiply(a, b):
    return a * b
def div(a, b):
    return a / b


while(True):

    cmd = input("input(a + b)>> ")
    cmds = cmd.split(" ")

    a = int(cmds[0])
    operator = cmds[1]
    b = int(cmds[2])
#함수단위로 빼보기
    if operator == "+":
        r = plus(a,b)

    elif operator == "-":
        r = minus(a,b)

    elif operator == "*":
        r = multiply(a,b)

    else:
        r = div(a,b)


    if operator in '+-*':
        print("Answer is {:d}".format(r))
    else:
        print("Answer is {:.2f} ".format(r))