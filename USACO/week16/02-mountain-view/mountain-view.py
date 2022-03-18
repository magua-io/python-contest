import sys

sys.stdin = open('mountains.in', 'r')
sys.stdout = open('mountains.out', 'w')

# key observations
# 1. the peak at (x, y) and the base are with 45 degree angles.
#    Therefore, the start of the base is at x-y, and the end of the base if at x+y.
# 2. As long as the mountain base is enclosed by another mountain, the peak is covered.
#
# Therefore, we just need to find how many mountains that are not enclosed by other mountains.

N = int(input())
mountains = []
for _ in range(N):
    x, y = map(int, input().split())
    mountains.append([x-y, x+y])
mountains.sort(key=lambda x: (x[0], -x[1]))

count = 0
i = 0
while i < N:
    count += 1
    start, end = mountains[i]
    i += 1
    while i < N and mountains[i][0] < end and mountains[i][1] <= end:
        i += 1

print(count)
