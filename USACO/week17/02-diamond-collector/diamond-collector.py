import sys

sys.stdin = open('diamond.in', 'r')
sys.stdout = open('diamond.out', 'w')

# Key Observation:
# You can't just pick the longest range, and find the second longest range
# [2, 2, 3, 3, 3, 4, 4] is the longest range with length 7
# [4, 4, 5, 5, 6, 6] or [0, 0, 1, 1, 2, 2] is the second longest range with length 6
# but if you pick [2, 2, 3, 3, 3, 4, 4],
# the rest longest range will be either [0, 0, 1, 1] or [5, 5, 6, 6]
# the sum will be 7 + 4 = 11
# However, if you pick two second longest ranges with length 6, the sum will be 6 + 6 = 12

N, K = map(int, input().split())
diamonds = []
for _ in range(N):
    diamonds.append(int(input()))
diamonds.sort()

# max number of diamonds in case when i is the largest diamond
amount_below = [0] * N
# max number of diamonds in case when i is the smallest diamond
amount_above = [0] * N

i = 0
j = 0

while j < N:
    if diamonds[j] - diamonds[i] <= K:
        amount_below[j] = j - i + 1
        amount_above[i] = j - i + 1
        j += 1
    else:
        i += 1

# Find max possible amount of diamonds in 2 cases.
res = 0
max_amount_below = 0


for i in range(1, N):
    max_amount_below = max(max_amount_below, amount_below[i-1])
    res = max(res, amount_above[i] + max_amount_below)

print(res)
