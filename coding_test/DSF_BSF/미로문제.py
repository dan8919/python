# N*M 미로에 갇혔으며 현재 위치는(1,1) 출구 (N,M) 괴물이 있는 부분은 0,없는
# 부분은 1,미로 탈출 하시오  1:07:00 참

from collections import  deque

n,m =map(int,input().split())
graph =[]
for i in range(n):
    graph.append(list(map(int,input())))

dx = [1,-1,0,0]
dy = [0,0,-1,1]



def bfs(x,y):
    queue =deque()
    queue.append((x,y))
    print ("queue:",queue)

    while queue:
        x,y =queue.popleft()
        print("while 문안에 queue:",queue)
        #현재 위치에서4가지 방향으로 위치 확인
        for i in range(4):
            nx =x+dx[i]
            ny =y+dy[i]
            #미로찾기 공간을 벗어난 경우 무시
            if nx<=-1 or nx>=n or ny<=-1 or ny>=m:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny] == 1:
                #??????????????????????왜서 +1
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[n-1][m-1]



print(bfs(1,1))
print(graph)
print (graph[1][1])


