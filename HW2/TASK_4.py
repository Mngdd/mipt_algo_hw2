def findCircleNum(isConnected: list[list[int]]) -> int:
    graph = [[ii for ii in range(len(isConnected[i])) if isConnected[i][ii]==1]
             for i in range(len(isConnected))]
    amount = 0

    visited = [False for _ in range(len(graph))]
    for v in range(len(graph)):
        if not visited[v]:
            amount += 1
            queue = [v]

            while len(queue) > 0:
                visiting_now = queue[-1]
                visited[visiting_now] = True
                finished_iterating = True

                for sub in graph[visiting_now]:
                    if not visited[sub]:
                        queue.append(sub)
                        finished_iterating = False
                        break
                if finished_iterating:
                    queue.pop(-1)

    return amount

print(findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))