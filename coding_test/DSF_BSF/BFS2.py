from collections import deque
#노드
vertexList = ['0', '1', '2', '3', '4', '5', '6']
#모든 연결 가능한 수를 전부 열거
edgeList = [(0, 1), (0, 2), (1, 0), (1, 3), (2, 0), (2, 4), (2, 5), (3, 1), (4, 2), (4, 6), (5, 2), (6, 4)]
#graph 정의
graph = (vertexList, edgeList)

def bfs(graph,start):
    vertexList,edgeList =graph
    #이미 방문한 노드 리스트
    visitedVertex = []
    #디큐를 사용하여 큐 형탱의 리스트->시작 노드 리스트에 입력
    queue = deque([start])
    #각 노드에 연결된 노드들의 집합으을 list로 만든 것
    adjacencyList = [[] for vertex in vertexList]


    for edge in edgeList:
        # 비어있던 adjacencyList를 채우기 시작. edge[0]->노드. edge[1]->연결된항
        adjacencyList[edge[0]].append(edge[1])

    #큐에 뭔가가 있을때 실행
    while queue:
        #큐 fifo 진행
        current = queue.popleft()
        #popleft한 노드의 연결항들이 방문했던 항이 아니면 큐에 넣어줌
        for neighbor in adjacencyList[current]:
            if not neighbor in visitedVertex:
                queue.append(neighbor)
        #popleft 한 항을 방문 리스트에 넣어줌
        visitedVertex.append(current)

    return visitedVertex

print(bfs(graph,0))