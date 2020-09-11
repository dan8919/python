
array = [4,3,6,5,8,1]

for i in range(1,len(array)):

    if array[0] > array[i]:
        temp = array[0]
        array[0] = array[i]
        array[i] = temp

    else:
        pass

    print (i,array)




