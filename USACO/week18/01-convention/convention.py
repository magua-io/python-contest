import sys

sys.stdin = open('convention.in', 'r')
sys.stdout = open('convention.out', 'w')


def validate(k, N, M, C, arrivals):
    """
    Check whether it is valid to wait maximum k unit of time.
    """

    # number of buses needed
    num_buses = 1
    # current cow on this bus
    cow = 1
    # earliest cow on this bus
    lcow = 0

    while cow < N:
        # can't satisfy time constraint by adding this cow
        if arrivals[cow] - arrivals[lcow] > k:
            lcow = cow
            num_buses += 1
        # can't fit this cow in the bus
        elif cow - lcow + 1 == C:
            lcow = cow + 1
            cow += 1
            if cow < N:
                num_buses += 1
        # add this cow to the current bus
        else:
            cow += 1

    return num_buses <= M


N, M, C = map(int, input().split())
arrivals = list(map(int, input().split()))

arrivals.sort()

lo = 0
# max wait time
hi = arrivals[-1] - arrivals[0]

# use binary search to find the minimum valid wait time
while lo < hi:
    mid = (lo + hi) // 2
    if validate(mid, N, M, C, arrivals):
        hi = mid
    else:
        lo = mid + 1

print(lo)
