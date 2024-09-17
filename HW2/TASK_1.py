def topological_sort(graph: list[list[int]]):
    ans = []

    visited = [False for _ in range(len(graph))]
    for v in range(len(graph)):
        if not visited[v]:
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
                    ans.append(visiting_now)

    return ans[::-1]