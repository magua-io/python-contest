def range_sum(x1, y1, x2, y2):
    """
    Calculate number of cows within the rectangle
    """
    return prefix_sum[x2+1][y2+1] - prefix_sum[x2+1][y1] - prefix_sum[x1][y2+1] + prefix_sum[x1][y1]


n = int(input())
prefix_sum = [[0] * (n+1) for _ in range(n+1)]
cows = []

for i in range(n):
    x, y = map(int, input().split())
    cows.append([x, y])

# reduce the empty space between cows
cows.sort()
for i in range(n):
    cows[i][0] = i + 1

cows.sort(key=lambda cow: cow[1])
for i in range(n):
    cows[i][1] = i + 1

for i in range(n):
    prefix_sum[cows[i][0]][cows[i][1]] = 1

# calculate 2D prefix sum
for i in range(1, n+1):
    for j in range(1, n+1):
        prefix_sum[i][j] += (
            prefix_sum[i-1][j]
            + prefix_sum[i][j-1]
            - prefix_sum[i-1][j-1]
        )

res = 0

# check all the cases, the number of subsets is
# (the number of cows can be selected as cow_c) * (the number of cows can be selected as cow_d)
# cow_c is the left side of rectangle, cow_d is the right side of the rectangle
for i in range(n):
    for j in range(i, n):
        xc = min(cows[i][0], cows[j][0]) - 1
        xd = max(cows[i][0], cows[j][0]) - 1
        res += range_sum(0, i, xc, j) * range_sum(xd, i, n-1, j)

# + 1 to include the empty subset
print(res + 1)
