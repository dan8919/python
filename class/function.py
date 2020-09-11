def fn():
    print("fn called")

# 함수를 부르면 메모리에 올려놓음,다시 부르면 메모리에서 찾음
fn()

def exp(x):
    return  x ** 2
exp3 = exp(3)
print(exp3)

def get_fruits():
    return ['a','b','c']
print(get_fruits()[0])

def get_name():
    return 'kim','Beck'

# 튜플로 받음 추가하거나 변경 불가능
name = get_name()
print(get_name())


def full_name(first_name,last_name):
    return first_name+" "+last_name
print(name,full_name('aaa','bbb'))

def var_param(a, *vp):
    print(type(vp))
    print(a, len(vp), vp[len(vp) - 1])
var_param("aa",'bbds')

def default_param(a,b = 'bbb'):
    print(a,b)
default_param('hello','kim')


#fecursive function재귀 함 내 로직을 내가 부르는
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
a = factorial(4)
print(a)

print(":::::::::::::::::::::::::::::::;")