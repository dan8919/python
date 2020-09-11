arr = [7,3,2,9]

def sum(arr,accu):
    print(arr,accu)

    if len(arr)==0: return  accu

    last = arr.pop() #제일 마지막 항 추
    result = last

    return  sum(arr, last+accu)


result = sum(arr,0)
print("result=>",  result)
print("arr=>",arr)