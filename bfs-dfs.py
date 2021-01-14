# https://www.acmicpc.net/problem/1260
from collections import deque


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for _v in graph[v]:
        if not visited[_v]:
            dfs(graph, _v, visited)


def bfs(graph, v, visited):
    visited[v] = True
    queue = deque([v])
    while queue:
        _v = queue.popleft()
        print(_v, end=' ')
        for __v in graph[_v]:
            if not visited[__v]:
                queue.append(__v)
                visited[__v] = True


if __name__ == "__main__":
    n, m, v = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    for i in range(m):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    for g in graph:
        g.sort()

    visited = [False] * (n+1)
    dfs(graph, v, visited)
    print()
    visited = [False] * (n+1)
    bfs(graph, v, visited)
