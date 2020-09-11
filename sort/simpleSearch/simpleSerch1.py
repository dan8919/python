#단순탐색
#장점: 쉽다,정렬이 안되어도 된다
#단점:느리다. ->대안:2진탐색(Binary Search)

arr =[1,2,3,4,5,6,7,8,11]
#8은 몇번째에 있을까요?
#입력받은 숫자가 몇번째 인덱스에 있는지

def search(arr,x):

    for index in range(0,len(arr)):
        if arr[index] == x:
           # print(arr[index])
            return index

    return -1




print(search(arr,8))
print(search(arr,100))