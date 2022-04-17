from collections import defaultdict
import sys
sys.setrecursionlimit(1000000)

N, M = map(int, input().split())
graph = defaultdict(set)
color = {}
visited = set()
is_bad = False

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)


def isBipartite(graph, color):
    for i in range(len(graph)):
        if (i) not in color:
            stack = [i]
            color[i] = 1
            while stack:
                node = stack.pop()
                for nei in graph[node]:
                    if nei not in color:
                        stack.append(nei)
                        color[nei] = 1 if color[node] == 2 else 2
                    elif color[nei] == color[node]:
                        return False
    return True


if not isBipartite(graph, color):
    print("IMPOSSIBLE")
else:
    for i in range(1, N+1):
        print(color[i])
