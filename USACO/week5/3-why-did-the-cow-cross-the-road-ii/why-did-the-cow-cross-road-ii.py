import sys

sys.stdin = open('circlecross.in', 'r')
sys.stdout = open('circlecross.out', 'w')

# Time complexity: O(N^2) where N = number of cows
# Space complexity: O(N)
line = input()

ins = [-1]*26
outs = [-1]*26

for i, c in enumerate(line):
  index = ord(c) - ord('A')
  if ins[index] == -1:
    ins[index] = i
  else:
    outs[index] = i

total = 0
for i in range(26):
  unique = set()
  if ins[i] == -1:
    continue
  for j in range(ins[i], outs[i]+1):
    if line[j] not in unique:
      unique.add(line[j])
    else:
      unique.remove(line[j])
  total += len(unique)

print(total // 2)