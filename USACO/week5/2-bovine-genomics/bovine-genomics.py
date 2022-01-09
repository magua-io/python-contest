import sys

sys.stdin = open('cownomics.in', 'r')
sys.stdout = open('cownomics.out', 'w')

# Time complexity: O(NM)
# Space complexity: O(M)
N, M = map(int, input().split())
spotty_cows = [set() for _ in range(M)]
plain_cows = [set() for _ in range(M)]

for _ in range(N):
  for i, c in enumerate(input()):
    spotty_cows[i].add(c)

for _ in range(N):
  for i, c in enumerate(input()):
    plain_cows[i].add(c)

count = 0
for i in range(M):
  # if len(plain_cows[i]) == 1 and len(spotty_cows[i] & plain_cows[i]) == 0:
  if len(spotty_cows[i] & plain_cows[i]) == 0:
    count += 1

print(count)