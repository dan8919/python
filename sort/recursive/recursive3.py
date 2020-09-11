arr = [7,3,2,9]

def sum(arr,accu):
    if len(arr)==0: return accu  #탈출조건, 끝에 꼭 넣어주어야 함.
    return  sum(arr, arr.pop()+accu)

print("result=>",  sum(arr,0))
