import sys

sys.stdin = open('lifeguards.in', 'r')
sys.stdout = open('lifeguards.out', 'w')


def get_coverage(slots):
    """
    count the coverage as long as the slot is positive.
    """
    count = 0
    for num in slots:
        if num > 0:
            count += 1
    return count


# read inputs
N = int(input())
shifts = []
for _ in range(N):
    shifts.append(list(map(int, input().split())))

# get the final time_slots
time_slots = [0] * 1000
for start, end in shifts:
    for i in range(start, end):
        time_slots[i] += 1

max_coverage = 0
# try to remove one of the shift and find the coverage
for start, end in shifts:
    new_time_slots = time_slots[:]
    for i in range(start, end):
        new_time_slots[i] -= 1
    # update the max_coverage if needed
    max_coverage = max(max_coverage, get_coverage(new_time_slots))

print(max_coverage)
