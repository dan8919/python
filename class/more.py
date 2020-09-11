lst=['오렌지','사과','배']
dic={'오렌지':400,'사과':200,'배':300}

for key in dic:
    print("key=", key, dic[key])

print(list(enumerate(lst)))


for i,value in enumerate(lst):
    print("tt=",i,value)
    print(lst[i])

for key,element in dic.items():
    print("items.key=", key, "element=", element)
###########################
lst = []
for i in range(0,20,2):
    i = i ** 2
    lst.append([i])



arr=[i ** 2 for i in range(0,20,2)]
print(arr)
print("최소값:",min(arr))
print("최대값:",max(arr))

#for 문 돌려서 f로 출려 단 '사과'가 아 인때#
lst = ['사과','배']
outs = [f for f in lst if f!='사과']
print(outs)

##############3
cmd =input ("Input>> ")
print(cmd)

cmds = cmd.split(" ")