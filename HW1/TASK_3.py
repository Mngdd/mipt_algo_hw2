def TASK_3(adjac_list: list[list[int]], v: int, u: int) -> bool:
    visited = [False for _ in range(len(adjac_list))]

    def dfs(from_: int, target: int) -> bool:
        visited[from_] = True
        if target in adjac_list[from_]: return True

        for v in adjac_list[from_]:
            if not visited[v] and dfs(v, target):
                return True

        return False

    return dfs(v, u) and dfs(u, v)