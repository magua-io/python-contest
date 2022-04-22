from collections import defaultdict
import sys

sys.stdin = open("wormsort.in", 'r')
sys.stdout = open("wormsort.out", 'w')
sys.setrecursionlimit(1000000)

N, M = map(int, input().split())
cows = list(map(int, input().split()))
for i in range(N):
    cows[i] -= 1

graph = defaultdict(list)

components = [-1] * N

for _ in range(M):
    a, b, w = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append([b, w])
    graph[b].append([a, w])


def dfs(v, label, min_width):
    components[v] = label

    for nei in graph[v]:
        nei, width = nei
        if width < min_width or components[nei] != -1:
            continue
        dfs(nei, label, min_width)


def ok(min_width):
    for i in range(N):
        components[i] = -1

    label = -1
    for i in range(N):
        if components[i] != -1:
            continue
        label += 1
        dfs(i, label, min_width)

    for i in range(N):
        if components[i] != components[cows[i]]:
            return False

    return True


res = -1
lo = 1
hi = 1e9 + 1
top = hi

while lo <= hi:
    mid = lo + (hi - lo) // 2
    if ok(mid):
        res = max(res, mid)
        lo = mid + 1
    else:
        hi = mid - 1

print(-1 if res == top else int(res))
