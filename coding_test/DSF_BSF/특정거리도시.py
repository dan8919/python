#n개 도시,m개 단방향 도로, 최단 거리가 k인 도시,x 도시에서 출발
#BFS 이용

from collections import deque

n,m,k,x = map(int,input().split())
#0,1,2,3...,n
#2차원 배열.1,도시 2,연결된 도시
graph = [[]for _ in range(n+1)]


for _ in range(m):
    #도로 정보 관련하여 입력 a:시작점 b: 도착
    a,b = map(int,input().split())
    graph[a].append(b)

#모든 도시 최단거리 초기화
#1차원 배열
distance = [-1]*(n+1)
distance[x] = 0


queue = deque([x])
while queue:

    current = queue.popleft()
    #현재 도시에서 이동할 수 있는 모든 도시 확인.(a의 모든 b 확인)
    for next_node in graph[current]:
        #아직 방문하지 않은 도
        if distance[next_node] ==-1:
            #최단 거리갱신
            distance[next_node] = distance[current]+1
            queue.append(next_node)

count = 0
for i in range(1,n+1):
    if distance[i]==k:
        print(i)
        count += 1

print(count)

