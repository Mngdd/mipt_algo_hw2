# Список ребер в список смежности
def edge_list_to_adjacency_list(edge_list, num_vertices):
    # для невзвешенного графа версия
    adjac_list = [[] for _ in range(num_vertices)]

    for u, v in edge_list:
        adjac_list[u].append(v)
        adjac_list[v].append(u)

    return adjac_list


# Матрица смежности в список смежности
def adjacency_matrix_to_adjacency_list(adjac_matrix):
    adjac_list = []

    for row in adjac_matrix:
        adjac_list.append([ind for ind, val in enumerate(row) if val])

    return adjac_list


# Список смежности в список ребер
def adjacency_list_to_edge_list(adjac_list):
    edge_list = []

    for ind, neighbors in enumerate(adjac_list):
        edge_list.extend([(ind, el) for el in neighbors
                          if (el, ind) not in edge_list])

    return edge_list


# Список ребер в матрицу смежности
def edge_list_to_adjacency_matrix(edge_list, num_vertices):
    # для невзвешенного графа версия
    adjac_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    for u, v in edge_list:
        adjac_matrix[u][v] = 1
        adjac_matrix[v][u] = 1

    return adjac_matrix


# Список смежности в матрицу смежности
def adjacency_list_to_adjacency_matrix(adjac_list):
    adjac_matrix = [[0 for _ in range(len(adjac_list))]
                    for _ in range(len(adjac_list))]

    for ind, neighbors in enumerate(adjac_list):
        for el in neighbors:
            adjac_matrix[ind][el] = 1

    return adjac_matrix


# Матрица смежности в список ребер
def adjacency_matrix_to_edge_list(adjac_matrix):
    edge_list = []

    for i in range(len(adjac_matrix)):
        edge_list.append([(i, j) for j in range(i + 1, len(adjac_matrix))
                          if adjac_matrix[i][j] == 1])

    return edge_list
