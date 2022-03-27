import heapq
import sys

sys.stdin = open('cowdance.in', 'r')
sys.stdout = open('cowdance.out', 'w')


def possible(dance_time, K, T):
    total_time = 0
    min_heap = []
    for t in dance_time:
        if len(min_heap) == K:
            total_time = heapq.heappop(min_heap)
        if total_time + t > T:
            return False
        heapq.heappush(min_heap, total_time + t)
    return True


N, T = map(int, input().split())
dance_time = []
for _ in range(N):
    dance_time.append(int(input()))

lo = 1
hi = N
while lo < hi:
    mid = (lo + hi) // 2
    if possible(dance_time, mid, T):
        hi = mid
    else:
        lo = mid + 1
print(lo)
