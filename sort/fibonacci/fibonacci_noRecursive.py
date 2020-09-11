
arr = []
#arr.append(1)
#arr.append(1)


def fib(n):

    for i in range(n):
        if i<2:
            arr.append(1)
        else:
            k = arr[i-2]+arr[i-1]
            arr.append(k)

    return arr

print(fib(100))



