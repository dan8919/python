def DFS_visit(adj,u,visited):
    visited.append(u)
    for v in adj[u]:
        if v not in visited:
            DFS_visit(adj,v,visited)

# def DFS(adj,s):
#     visited = []
#     DFS_visit(adj,s,visited)
#     print(adj)
#     return visited
#{ } 집합 자료형(중복 허용하지 않고 순서가 없음)
G1 = {1:[2,3],2:[3,4,5],3:[5,7,8],4:[5],5:[6],6:[],7:[8],8:[]}




def DFS(adj,s):
    tovisit =[s]
    visited =[]
    while tovisit:
        u = tovisit.pop()
        visited.append(u)
        for v in adj[u]:
            if v not in visited+tovisit:
                tovisit.append(v)
    return visited
#print (DFS2(G1,1))

print(DFS(G1,1))