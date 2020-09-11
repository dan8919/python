#2.삽입 정렬:첫 번째 항과 그 앞에  항들과 비교하여 자리바꿈

array = [3,4,6,7,2,1,5,11,21]

for i in range(1,len(array)):
    for j in range(i,0,-1):
        if array[j]>array[j-1]:
            array[j],array[j-1] = array[j-1],array[j]
        else:break




print(array)
