import sys

sys.stdin = open('revegetate.in', 'r')
sys.stdout = open('revegetate.out', 'w')

N, M = map(int, input().split())
res = [1] * N

adj = [[] for _ in range(N)]
taken = [[False]*4 for _ in range(N)]

for _ in range(M):
  p1, p2 = map(int, input().split())
  adj[p1-1].append(p2-1)
  adj[p2-1].append(p1-1)

for i in range(N):
  for j in range(4):
    if not taken[i][j]:
      res[i] = j + 1
      for k in adj[i]:
        taken[k][j] = True
      break

print(''.join([str(x) for x in res]))
