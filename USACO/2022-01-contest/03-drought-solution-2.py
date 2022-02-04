# Solution 2
def get_operations(hungers, i, num_op):
    if num_op < 0:
        return -1
    hungers[i] -= num_op
    hungers[i + 1] -= num_op
    return 2 * num_op


def find_minimum_bags_of_corn(n, hungers):
    res = 0
    flag = True
    while flag:
        flag = False
        for i in range(n - 1):
            if hungers[i] != hungers[i + 1]:
                flag = True
                if hungers[i + 1] > hungers[i]:
                    if i + 1 == n - 1:
                        return -1
                    tmp = get_operations(
                        hungers, i + 1, hungers[i + 1] - hungers[i])
                    if tmp == -1:
                        return -1
                    res += tmp
                else:
                    if i == 0:
                        return -1
                    tmp = get_operations(
                        hungers, i - 1, hungers[i] - hungers[i + 1])
                    if tmp == -1:
                        return -1
                    res += tmp
                break

    return res if hungers[0] >= 0 else -1


num_test = int(input())
while num_test > 0:
    n = int(input())
    hungers = list(map(int, input().split()))
    print(find_minimum_bags_of_corn(n, hungers))
    num_test -= 1
