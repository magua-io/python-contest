import sys

sys.stdin = open('speeding.in', 'r')
sys.stdout = open('speeding.out', 'w')

N, M = map(int, input().split())
road_segments = []
bessie_segments = []

for _ in range(N):
  road_segments.append(list(map(int, input().split())))
for _ in range(M):
  bessie_segments.append(list(map(int, input().split())))

limit = []
bessie = []

for s in road_segments:
  for _ in range(s[0]):
    limit.append(s[1])

for s in bessie_segments:
  for _ in range(s[0]):
    bessie.append(s[1])

max_over = 0
for a, b in zip(limit, bessie):
  max_over = max(max_over, b-a)
print(max_over)
