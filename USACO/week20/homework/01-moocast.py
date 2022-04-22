import sys

sys.stdin = open("moocast.in", 'r')
sys.stdout = open("moocast.out", 'w')


def dfs(v):
    visited[v] = True
    count = 1
    for u in range(n):
        if visited[u] or not canReach[v][u]:
            continue
        count += dfs(u)
    return count


n = int(input())
x = [0] * n
y = [0] * n
p = [0] * n
for i in range(n):
    x[i], y[i], p[i] = map(int, input().split())

canReach = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        squaredDistance = (x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2
        squaredRange = p[i] ** 2
        canReach[i][j] = squaredDistance <= squaredRange

ans = 0
for i in range(n):
    visited = [0] * n
    ans = max(ans, dfs(i))

print(ans)
