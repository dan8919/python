#인덱스 번호와 컬렉션의 원소를 tuple 형태로 반환
#튜플()
t = [1,5,7,33,39,52]
for p in enumerate(t):
    print(p)




for i,v in enumerate(t):
    print("index:{},value:{}".format(i,v))


visited = []
def DFS_visit(adj,u,visited):

    visited.append(u)
    for v in adj[u]:
        if v not in visited:
            DFS_visit(adj,v,visited)
    return visited


G1 = {1:[2,3],2:[3,4,5],3:[5,7,8],4:[5],5:[6],6:[],7:[8],8:[]}
print(DFS_visit(G1,1,visited))


#type : list 3,4,5
print(type(G1[2]))
#type : dict { }  immutable 한 key  mutable 한 value
#순서가 없기 때문에 인덱스로 접근할수 없고 키로 접근 할 수 있습니다.
#dic : key 로 value 확인  G1[key]

# https://wikidocs.net/16043
print(type(G1))

#[]가 5개 들어간 배열 만들기
k =[[]for _ in range(5)]
print(k)