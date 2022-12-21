graph = {
    'a': ['b'],
    'b': ['e'],
    'c': ['d'],
    'd': [],
    'e': ['d']
}

"""
a -> b -> e ->  d
                ^
                |
                c
"""


def hasPathDFS(graph, src, dest):
    if src == dest:
        return True

    for neighbor in graph[src]:
        if hasPathDFS(graph, neighbor, dest):
            return True
    return False


def hasPathBFS(graph, src, dest):
    q = [src]
    while q:
        curr = q.pop()

        if curr == dest:
            return True

        for neighbor in graph[curr]:
            q.append(neighbor)

    return False


print(hasPathDFS(graph, 'a', 'e'))
print(hasPathDFS(graph, 'a', 'c'))
print(hasPathBFS(graph, 'a', 'e'))
print(hasPathBFS(graph, 'a', 'c'))
