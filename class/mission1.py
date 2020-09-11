#1.1부터 100까지의 합을 구하시오#
sum=0;
for i in range(101):
    sum += i
print(sum,i)

sum1,i = 0,1
while (i<=100):
    sum1 += i
    i += 1
print(sum1)





#1.1부터 100까지의 홀수의 합을 구하시오#
sum2,i =0,0
while (i>=0):
    i += 1

    a=i
    if (i%2==0):
        continue
    if (i>100):
        break
    b = i
    sum2 += i


print(sum2,i,a,b)

sum3,i=0,0
while (i<101):
    if(i%2==1):
        sum3 += i
    i += 1
print(sum3)