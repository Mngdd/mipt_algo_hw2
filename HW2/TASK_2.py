from TASK_1 import topological_sort

vertices = ["Пиджак", "Часы", "Брюки", "Рубашка", "Трусы", "Носки", "Туфли", "Галстук", "Ремень"]

connections = [[], [], [6, 8], [8, 7], [2, 6], [6], [], [0], [0]]

print(*[vertices[i] for i in topological_sort(connections)])
