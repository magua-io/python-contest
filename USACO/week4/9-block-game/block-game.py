import sys

sys.stdin = open("blocks.in", "r")
sys.stdout = open("blocks.out", "w")

# Time complexity: O(N)

def count_frequency(s):
  freqs = [0] * 26
  for c in s:
    freqs[ord(c) - ord('a')] += 1
  return freqs

N = int(input())
# output result to store the maximum letters needed
res = [0] * 26
for _ in range(N):
  s1, s2 = input().split()
  # count the frequency of letters for each side of card
  freq1, freq2 = count_frequency(s1), count_frequency(s2)
  # for each letter, use the maximum number from the two sides
  for i in range(26):
    res[i] += max(freq1[i], freq2[i])

# output
for freq in res:
  print(freq)
