# Solution 3
def find_minimum_bags_of_corn(n, hungers):
    if n == 1:
        return 0
    res = 0
    for _ in range(2):
        for i in range(1, n - 1):
            if hungers[i] > hungers[i - 1]:
                diff = hungers[i] - hungers[i - 1]
                res += 2 * diff
                hungers[i + 1] -= diff
                hungers[i] = hungers[i - 1]
        if hungers[-1] > hungers[-2]:
            return -1
        hungers = hungers[::-1]

    return -1 if hungers[0] < 0 else res


num_test = int(input())
while num_test > 0:
    n = int(input())
    hungers = list(map(int, input().split()))
    print(find_minimum_bags_of_corn(n, hungers))
    num_test -= 1
