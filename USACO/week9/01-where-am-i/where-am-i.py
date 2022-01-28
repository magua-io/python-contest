import sys

sys.stdin = open('whereami.in', 'r')
sys.stdout = open('whereami.out', 'w')

N = int(input())
mailboxes = input()

res = N

# We can iterate through lengths of sequences to find the smallest length
for K in range(1, N+1):
  # Store the substrings in a set
  sequences = set()
  for start in range(N+1-K):
    sequences.add(mailboxes[start:start+K])
  # Check if all substrings are unique
  if len(sequences) == N+1-K:
    res = K
    # We can exit the loop as this will be the smallest working length
    break

print(res)