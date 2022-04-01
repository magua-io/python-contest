from math import ceil
import sys

sys.stdin = open('angry.in', 'r')
sys.stdout = open('angry.out', 'w')


def validate(R, K, hay_bales):
    """
    to check whether radius R is valid to detonate all the hay bales.
    """
    # number of cows needed
    num_cows = 1
    # current hay
    hay = 0
    # left most hay to include for current cow
    lhay = 0

    while hay < len(hay_bales):
        if hay_bales[hay] - hay_bales[lhay] > 2 * R:
            lhay = hay
            num_cows += 1
        else:
            hay += 1
    return num_cows <= K


N, K = map(int, input().split())
hay_bales = []
for _ in range(N):
    hay_bales.append(int(input()))

hay_bales.sort()
lo = 0
hi = hay_bales[-1] - hay_bales[0]

# use binary search to find the minimum R
while lo < hi:
    mid = (lo + hi) // 2
    if validate(mid, K, hay_bales):
        hi = mid
    else:
        lo = mid + 1

print(lo)
