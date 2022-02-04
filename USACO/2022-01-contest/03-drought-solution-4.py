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

    """
    f + o0 = h0
    f + o0 + o1 = h1
    f + o1 + o2 = h2
    f + o2 + o3 = h3
    ...
    f + o(N-3) + O(N-2) = h(N-2)
    f + o(N-2) = h(N-1)

    o0 = h0 - f
    o1 = h1 - o0 - f
    o2 = h2 - o1 - f
    o3 = h3 - o2 - f
    ...
    o(N-2) = h(N-1) - f

    o0 = h0 - f
    o1 = h1 - o0 - f = h1 - (h0 - f) -f = h1 - h0
    o2 = h2 - o1 - f = h2 - (h1 - h0) - f = h2 - h1 + h0 -f
    o3 = h3 - o2 - f = h3 - (h2 - h1 + h0 - f) - f = h3 - h2 + h1 - h0
    ...
    o(N-2) = h(N-1) - o(N-2) - f

    if N-2 is odd, which means N is odd
        o(N-2) = h(N-1) - h(N-2) + h(N-3) - ... + h1 - h0
    if N-2 is even, which means N is even
        o(N-2) = h(N-1) - h(N-2) + h(N-3) - ... - h1 + h0 -f

    Therefore, if N odd, maximize f can decrease o(0), o(2), O(4), ..., O(N-1)
    max_f = min(o(0), o(2), O(4), ..., O(N-1)
    """
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
