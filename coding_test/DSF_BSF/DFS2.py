
#노드
vertexList = ['0', '1', '2', '3', '4', '5', '6']
#모든 연결 가능한 수를 전부 열거
edgeList = [(0, 1), (0, 2), (1, 0), (1, 3), (2, 0), (2, 4), (2, 5), (3, 1), (4, 2), (4, 6), (5, 2), (6, 4)]
#graph 정의
graphs = (vertexList, edgeList)


def dfs(graph, start):
    vertexList, edgeList = graph
    #이미 방문한 노드 리스트
    visitedVertex = []
    #스택으로정의-> 시작 노드 리스트에 입력
    stack = [start]
    #각 노드에 연결된 노드들의 집합을 list로 만든 것
    adjacencyList = [[] for vertex in vertexList]


    #노드 리스트의 연결된상황 예:(0,1),(0,2)
    for edge in edgeList:
        #비어있던 adjacencyList를 채우기 시작. edge[0]->노드. edge[1]->연결된항
        adjacencyList[edge[0]].append(edge[1])
        print("edge:",edge)
        print("0:",edge[0])
        print("1:",[edge[1]])
        print(adjacencyList)
    #스택에 뭔가가 있을때 실행 .[start]로 시작
    while stack:
        #스택 lifo 진행
        current = stack.pop()
        #lifo 스택에서 pop한 것의 모든 연결된 항들을 neighbor에 넣어봄
        for neighbor in adjacencyList[current]:
            #이미 방문한 노드가 아니면 스택에 추가해 줌
            if not neighbor in visitedVertex:
                stack.append(neighbor)
        #스택에서 pop한 노드를 이미 방문한 노드리스트에 넣어줌
        visitedVertex.append(current)
    return visitedVertex


print(dfs(graphs, 0))
