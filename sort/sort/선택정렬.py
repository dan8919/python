
#1.선택 정렬: 가장 작은 데이터를 제일 앞에 숫자와 바꾸는 것
array = [3,4,6,7,2,8,11,21]

for i in range(len(array)):
    min_index = i
    for j in range(i+1,len(array)):
        if array[min_index]>array[j]:
            min_index = j
        array[i],array[min_index] = array[min_index],array[i]

print(array)
