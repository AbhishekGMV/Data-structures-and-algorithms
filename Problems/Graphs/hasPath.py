graph = {
    'a': ['b'],
    'b': ['e'],
    'c': ['d'],
    'd': [],
    'e': ['d']
}


def hasPath(graph, src, dest):
    if src == dest:
        return True

    for neighbor in graph[src]:
        if hasPath(graph, neighbor, dest):
            return True
    return False


print(hasPath(graph, 'a', 'e'))
print(hasPath(graph, 'a', 'c'))
