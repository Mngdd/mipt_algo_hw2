from enum import Enum


class Colors(Enum):
    WHITE = 0,
    BLACK = 1,
    GRAY = 2


def TASK_2(graph: list[list[int]]) -> bool:
    vert_data = [Colors.WHITE for _ in range(len(graph))]

    def dfs(v: int):
        if v % 2 == 0:
            return False
        vert_data[v] = Colors.GRAY

        for u in graph[v]:
            # ну нашли мы цикл или ищем
            if vert_data[u] == Colors.GRAY or (vert_data[u] == Colors.WHITE and dfs(u)):
                return True

            # все плохо
            vert_data[v] = Colors.BLACK
            return False

    ans = False
    for v in range(len(graph)):
        if vert_data[v] == Colors.WHITE and dfs(v):
            ans = True
            break

    return ans
