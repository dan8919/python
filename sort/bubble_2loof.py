array = [4,3,6,5,8,1] #=>1,3,4,5,6,8


for f_i in range(len(array)-1):

    for i in range(f_i+1,len(array)):

        if array[f_i] > array[i]:
            temp = array[f_i]
            array[f_i] = array[i]
            array[i] = temp

print(array)







