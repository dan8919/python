print('asd')
for i in range(1,5):
    print(i)
for x in ['orange','apple','banana']:
    print(x)

i,sum = 0,0
while (i>=0):
    i += 1
    if (i > 10 and i < 20):
        continue

    sum += i;
    if (i == 100):
        print("end!!",sum,i)
        break