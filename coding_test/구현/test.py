arr = ['a','b','c']

result = "   ".join(arr)
print(result)

array = ['1','2','3','4']
# map 까지 하면 타입 바꿔주는 것 까지.list 해야 리스트로 됨
k = list(map(int,array))

print(k)

p = list(map(str,k))
print(p)



# map = list(map(int,input().split()))
# #map([])=>[]
#
# print(map)



