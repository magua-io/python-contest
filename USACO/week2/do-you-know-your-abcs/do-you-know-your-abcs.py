# read input
arr = list(map(int, input().split()))
# sort the array so that it is easy to get the 1st, 2nd and 3rd greatest numbers
arr.sort()

# It is known that A <= B <= C
# Find A+B+C, which should be the greatest value
max1 = arr[-1]
# Find the second and third greatest values
max2 = arr[-2]
max3 = arr[-3]
# A = (A+B+C) - second greatest
A = max1 - max2
# B = (A+B+C) - third greatest
B = max1 - max3
# C = (A+B+C) - A - B
C = max1 - A - B

# output
print(A, B, C)