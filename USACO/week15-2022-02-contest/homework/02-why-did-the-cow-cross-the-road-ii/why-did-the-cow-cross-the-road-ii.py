import sys

sys.stdin = open('maxcross.in', 'r')
sys.stdout = open('maxcross.out', 'w')

# Solution 1: prefix sum
N, K, B = map(int, input().split())
broken_roads = [0] * (N + 1)
prefix_sum = [0]

for _ in range(B):
    broken_roads[int(input())] = 1

for i in range(N):
    prefix_sum.append(broken_roads[i+1] + prefix_sum[i])

res = float('inf')
for i in range(N-K+1):
    res = min(res, prefix_sum[i + K] - prefix_sum[i])

print(res)


# Solution 2: sliding window
# N, K, B = map(int, input().split())
# roads = [1] * N
# left = 0
# right = 0

# for _ in range(B):
#     roads[int(input()) - 1] = 0

# num_repair = 0
# min_num_repair = float('inf')
# for i, num in enumerate(roads):
#     if num == 0:
#         num_repair += 1
#     if i >= K:
#         if roads[i-K] == 0:
#             num_repair -= 1
#         min_num_repair = min(min_num_repair, num_repair)

# print(min_num_repair)
