arr = [7,3,2,9]

def sum(arr):
    last = arr.pop() #제일 마지막 항 추
    print(last)
    result = arr[0]+arr[1]+last#7+3+9


    last = arr.pop()
    result = result+last #7+3+9+2
    print("last2=> ",last)
    return  result


result = sum(arr)
print("result=>", result)
print(arr)
