def findJudge(n: int, trust: list[list[int]]) -> int:
    trust_data = dict()
    isolated = [i for i in range(1, n + 1)]

    for key, val in trust:
        if key not in trust_data:
            trust_data[key] = []
            isolated.pop(isolated.index(key))
        trust_data[key].append(val)

    if (len(isolated) != 1):
        return -1

    for key in range(1, n + 1):
        if key == isolated[0]:
            continue
        if isolated[0] not in trust_data[key]:
            return -1
    return isolated[0]
