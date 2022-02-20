import sys

sys.stdin = open('taming.in', 'r')
sys.stdout = open('taming.out', 'w')

N = int(input())
logs = list(map(int, input().split()))

# The first entry in the log is a special case,
# since Farmer John already knows the cows broke out on that day.
if logs[0] > 0:
    print(-1)
    exit()

# We can always set logs[0] as 0
logs[0] = 0
# unset as -1
num_to_fill = -1
num_zeros_for_sure = 0
num_potential_zeros = 0


# If we ever come across a contradiction, then the
# log is necessarily inconsistent, so we can just output −1.
# Otherwise, the log must consist of several streaks 0,1,2,…,k
# of various lengths, with possibly some −1s between
# streaks - entries which we could not uniquely deduce.
# We know that the first streak starts on the first day.

for i in range(N-1, -1, -1):
    if num_to_fill != -1 and logs[i] != -1 and logs[i] != num_to_fill:
        print(-1)
        exit()
    if num_to_fill == -1:
        num_to_fill = logs[i]
    # if logs[i] is unset, set it as num_to_fill
    if logs[i] == -1:
        logs[i] = num_to_fill

    # update num_zeros_for_sure or num_potential_zeros
    if logs[i] == 0:
        num_zeros_for_sure += 1
    elif logs[i] == -1:
        num_potential_zeros += 1

    # decrease num_to_fill as needed
    if num_to_fill != -1:
        num_to_fill -= 1

print(num_zeros_for_sure, num_zeros_for_sure + num_potential_zeros)
