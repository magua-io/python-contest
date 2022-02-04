# Solution 1
def cost(n, hungers, min_hunger):
    bags = 0
    n = len(hungers)
    for i in range(n - 1):
        if hungers[i] > min_hunger:
            diff = min(hungers[i], hungers[i + 1]) - min_hunger
            hungers[i] -= diff
            hungers[i + 1] -= diff
            bags += 2 * diff
    for i in range(n-1):
        if hungers[i] != hungers[i + 1]:
            return float('inf')
    return bags


def find_minimum_bags_of_corn(n, hungers):
    min_hunger = min(hungers)
    min_res = float('inf')
    for i in range(min_hunger+1):
        min_res = min(min_res, cost(n, hungers[:], i))
    return -1 if min_res == float('inf') else min_res


num_test = int(input())
while num_test > 0:
    n = int(input())
    hungers = list(map(int, input().split()))
    print(find_minimum_bags_of_corn(n, hungers))
    num_test -= 1
