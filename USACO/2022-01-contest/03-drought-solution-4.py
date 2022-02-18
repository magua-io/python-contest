# Solution 4
def find_minimum_bags_of_corn(n, hungers):
    f = 0
    for i in range(n):
        if i % 2 == 0:
            f += hungers[i]
        else:
            f -= hungers[i]

    if n % 2 == 0:
        if f != 0:
            return -1
    else:
        if f < 0:
            return -1

    o = [0] * (n - 1)
    for i in range(n - 1):
        o[i] = hungers[i] - f - o[i-1]
        if o[i] < 0:
            return -1

    if n % 2 == 0:
        min_among_even = o[0]
        for i in range(2, n, 2):
            min_among_even = min(min_among_even, o[i])
        for i in range(0, n, 2):
            o[i] -= min_among_even

    return 2 * sum(o)


num_test = int(input())
while num_test > 0:
    n = int(input())
    hungers = list(map(int, input().split()))
    print(find_minimum_bags_of_corn(n, hungers))
    num_test -= 1
