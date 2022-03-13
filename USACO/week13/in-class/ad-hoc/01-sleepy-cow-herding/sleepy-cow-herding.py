import sys

sys.stdin = open('herding.in', 'r')
sys.stdout = open('herding.out', 'w')

a, b, c = map(int, input().split())

# Best scenario: the three elements are already in order.
if c == a + 2:
    print(0)

# If there is a difference by 2, it can be solved in one move.
# 3 5 9 -> 5 7 9
elif b == a + 2 or c == b + 2:
    print(1)

# It can always be solved in two moves by moving a -> c - 2 and b -> c - 1.
# If there is less than one integer between the two elements, it'll be taken care
# of in the if statement above.
else:
    print(2)

# The worst case is incrementing by 1 in the largest gap.
# 3 5 9 -> 5 6 9 -> 6 7 9 -> 7 8 9
print(max(b - a, c - b) - 1)
