import sys

sys.stdin = open('socdist.in', 'r')
sys.stdout = open('socdist.out', 'w')


def validate(D, N, intervals):
    """
    Check whether is valid to use distance D to keep social distance.
    """
    num_cows = 1
    interval = 0
    pos = intervals[0][0]

    for interval in intervals:
        while pos + D <= interval[1]:
            num_cows += 1
            pos = max(pos + D, interval[0])
            if num_cows == N:
                return True
    return False


N, M = map(int, input().split())
intervals = []
for _ in range(M):
    intervals.append(list(map(int, input().split())))

intervals.sort()

lo = 1
hi = intervals[-1][1] - intervals[0][0]

# use binary search to find the maximum valid social distance
while lo < hi:
    mid = (lo + hi + 1) // 2
    if validate(mid, N, intervals):
        lo = mid
    else:
        hi = mid - 1

print(lo)
