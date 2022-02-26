import sys

sys.stdin = open('balancing.in', 'r')
sys.stdout = open('balancing.out', 'w')


def count_cows_in_four_region(cows, a, b):
    """
    count cows in each region with provided a and b
    """
    count_bottom_left = 0
    count_bottom_right = 0
    count_top_left = 0
    count_top_right = 0
    for x, y in cows:
        if x < a and y < b:
            count_bottom_left += 1
        elif x > a and y > b:
            count_top_right += 1
        elif x < a and y > b:
            count_top_left += 1
        else:
            count_bottom_right += 1

    return count_top_left, count_top_right, count_bottom_left, count_bottom_right


# read inputs
N, B = map(int, input().split())
cows = []
for _ in range(N):
    cows.append(list(map(int, input().split())))

# initalize M as all the cows
M = N
# try to put fence at every position of x+1 and y+1
for x, _ in cows:
    a = x + 1
    for _, y in cows:
        b = y + 1
        # find out the max value among four parts,
        # and update the mim(M) if possible
        M = min(M, max(count_cows_in_four_region(cows, a, b)))

print(M)
