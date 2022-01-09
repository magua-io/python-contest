import sys

sys.stdin = open('gymnastics.in', 'r')
sys.stdout = open('gymnastics.out', 'w')

# Time complexity: O(KN^2)
# Space complexity: O(N^2)

K, N = map(int, input().split())
sets = []
for _ in range(K):
  my_set = set()
  my_list = list(map(int, input().split()))
  for i in range(N):
    for j in range(i+1, N):
      my_set.add((my_list[i], my_list[j]))
  sets.append(my_set)

union = sets[0]
for i in range(1, len(sets)):
  union &= sets[i]


print(len(union))