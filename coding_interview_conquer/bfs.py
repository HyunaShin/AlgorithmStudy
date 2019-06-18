vertex_list = ["A", "B", "C", "D", "E", "F", "G"]
edge_list = [(0,1), (1,2), (1,3), (3,4), (4,5), (1,6)]
graphs = (vertex_list, edge_list)

def bfs(graph , start):
    '''
    너비 우선 탐색은 queue를 활용한 탐색법이다.
    방법은 다음과 같다.
    1. 시작 노드를 정한다.
    2. 노드를 큐에 넣는다.
    3. dequeue한다. --> dequeue한 노드의 인접 노드를 queue에 넣는다.이 때 이미 방문한 노드는 무시한다.
    4. dequeue한 노드를 visited에 넣는다.
    응용하면, 최단 경로를 구할 때 쓴다.
    '''
    vertex_list, edge_list = graph
    visited_list = []
    queue = [start]
    adjacency_list = [[] for vertex in vertex_list]
    for edge in edge_list:
        adjacency_list[edge[0]].append(edge[1])

    while queue:
        current = queue.pop(0)
        # current = queue.pop()
        for neighbor in adjacency_list[current]:
            if neighbor not in visited_list:
                queue.append(neighbor)
                # queue.insert(0,neighbor)
        visited_list.append(current)
    return visited_list

print(bfs(graphs,0))
