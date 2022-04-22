import sys
from collections import defaultdict

sys.stdin = open("revegetate.in", 'r')
sys.stdout = open("revegetate.out", 'w')
sys.setrecursionlimit(1000000)

N, M = map(int, input().split())
single_graph = defaultdict(list)
double_graph = defaultdict(list)
impossible = False
answer = 0
L = [0] * (N + 1)


def visit(x, v):
    L[x] = v
    for nei in single_graph[x]:
        if L[nei] == 2:
            impossible = True
        if L[nei] == 0:
            visit(nei, v)

    for nei in double_graph[x]:
        if L[nei] == v:
            impossible = True
        if L[nei] == 0:
            visit(nei, 1)


for _ in range(M):
    type, a, b = input().split()
    a = int(a)
    b = int(b)
    if type == 'S':
        single_graph[a].append(b)
        single_graph[b].append(a)
    elif type == 'D':
        double_graph[a].append(b)
        double_graph[b].append(a)

for i in range(1, N+1):
    if L[i] == 0:
        visit(i, 1)
        answer += 1

if impossible:
    print(0)
else:
    print('1' + '0'*answer)
