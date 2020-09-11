#알파벳은 오름차 순으로 정렬하고 숫자는 더해서 뒤에 추가

data = input()
result = []
value = 0


#문자와 숫자 분간df
for i in data:
    if i.isalpha():
        result.append(i)
    else:
        value += int(i)


result.sort()
if value != 0:
    result.append(str(value))


print(result)
print("".join(result))
print(result)