import sys

sys.stdin = open('shell.in', 'r')
sys.stdout = open('shell.out', 'w')

N = int(input())
shells = [0, 1, 2]
counter = [0, 0, 0]

for _ in range(N):
  a, b, g = map(int, input().split())
  # swap shells positions (needs to -1 on a and b because a and b's values are in the range of [1, 3]
  # but python list `shells` is zero-indexing
  shells[a-1], shells[b-1] = shells[b-1], shells[a-1]
  counter[shells[g-1]] += 1

print(max(counter))