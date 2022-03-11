import sys

sys.stdin = open('div7.in', 'r')
sys.stdout = open('div7.out', 'w')

N = int(input())
max_count = 0
prefix_sum_mod = 0
prefix_sum_mods = [-1] * 7
# initial prefix_sum_mods[0] as 0
prefix_sum_mods[0] = 0

for i in range(N):
    cow = int(input())
    prefix_sum_mod = (prefix_sum_mod + cow) % 7
    # store the first occurrence of the prefix_sum_mod with the smallest index i
    if prefix_sum_mods[prefix_sum_mod] == -1:
        prefix_sum_mods[prefix_sum_mod] = i
    else:
        max_count = max(max_count, i - prefix_sum_mods[prefix_sum_mod])

print(max_count)
