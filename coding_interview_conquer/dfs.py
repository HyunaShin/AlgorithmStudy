
vertex_list = ['0', '1', '2', '3', '4','5','6']
edge_list = [(0,1), (0,2), (1,0), (1,3), (2,0),(2,4), (2,5), (3,1), (4,2), (4,6), (5,2), (6,4)]
adjacency_list = [[] for vertex in vertex_list]
graphs = (veretex_list, edge_list)

def dfs(graph, start):
    '''
    깊이 우선 탐색은, stack을 이용한 탐색 방법
    1. 시작 노드를 정한다.
    2. 노드를 stack에 넣는다.
    3. pop으로 stack에서 노드를 꺼낸다
    4. stack에 3번에서 pop한 노드의 인접 노드를 넣는다.(이 때 이미 방문한 노드는 무시한다.)
    5. 이미 pop한 노드를 visited(방문한 노드의 리스트)에 넣는다.
    이를 응용하면 그래프 내의 사이클 찾기를 할 수 있다.
    visited에 중복된 노드가 있다 --> 그래프 내의 사이클이 존재한다.
    '''
    vertex_list, edge_list = graph
    visited_vertex = []
    stack = [start] #1,2
    adjacency_list = [[] for vertex in veretex_list]

    for edge in edge_list:
        adjacency_list[edge[0]].append(edge[1])
    while stack:

        current = stack.pop() #3
        #4
        for neighbor in adjacency_list:
            if not neighbor in visited_vertex:
                stack.append(neighbor)
        visited_vertex.append(current) #5
    return visited_vertex
