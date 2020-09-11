#이진탐색(binary search)
#장점:빠름 o(log 100/log 80...)
#단점:정렬이 되어있어야 한다. 만들기 어렵다

#핵심로직
#*중간인덱스값을 구한다 10억개 -> 5억개
#*현재 중간값과 비교 크면 오른쪽 선택 작으면 왼쪽

arr = [1,2,3,4,5,6,7,8,11]
def binarySearch(arr,targetNum):
    start = 0
    end = len(arr)-1

    while(start <= end):

        midIndex = (start+end+1)//2 #몫만 구하느것
        indexValue = arr[midIndex]
        if indexValue == targetNum:
            return midIndex
        elif indexValue < targetNum:
            start = midIndex + 1

        else:
            end = midIndex - 1


        print("start:",start,"end:",end)
    return -1

print(binarySearch(arr,100))



