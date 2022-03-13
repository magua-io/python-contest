import sys

sys.stdin = open('outofplace.in', 'r')
sys.stdout = open('outofplace.out', 'w')

# Solution 1
# Time: O(n)
# Space: O(1)

n = int(input())
line = []
for _ in range(n):
    line.append(int(input()))

# find  Bessie position
bessie = 0
move_left = True
for i, h in enumerate(line):
    if i == 0 and h > line[i + 1]:
        # 9 1 2
        # i
        bessie = 0
        move_left = False
        break
    if i > 0 and h < line[i - 1]:
        if i == n - 1:
            # 5 6 4
            #     i
            bessie = i
            break
        if i > 0 and line[i - 1] <= line[i + 1]:
            # 7 6 7
            #   i
            bessie = i
            break
        else:
            # 7 5 6
            #   i
            bessie = i - 1
            move_left = False
            break

count = 0

if move_left:
    # try to move left
    i = bessie - 1
    while i >= 0 and line[i] > line[bessie]:
        count += 1
        # skip identical height
        while i > 0 and line[i - 1] == line[i]:
            i -= 1
        i -= 1
else:
    # try to move right
    i = bessie + 1
    while i + 1 < n and line[bessie] > line[i]:
        count += 1
        # skip identical height
        while i + 1 < n and line[i + 1] == line[i]:
            i += 1
        i += 1

print(count)


# Solution 2
# Time: O(nlogn)
# Space: O(n), space used by Timsort

n = int(input())
line = []
for _ in range(n):
    line.append(int(input()))

ordered_line = sorted(line)

diff = 0
# find differences between line and ordered_line
for i in range(n):
    if line[i] != ordered_line[i]:
        diff += 1

# diff - 1 is the swaps needed
print(diff - 1)
