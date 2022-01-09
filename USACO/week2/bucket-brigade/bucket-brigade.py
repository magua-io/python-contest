import sys
sys.stdin = open('buckets.in', 'r')
sys.stdout = open('buckets.out', 'w')

# get locations for B, R and L
for i in range(10):
  row = input()
  for j in range(10):
    if row[j] == 'B':
      B_i, B_j = i, j
    elif row[j] == 'R':
      R_i, R_j = i, j
    elif row[j] == 'L':
      L_i, L_j = i, j

# the distance between B and L
distance = abs(B_i - L_i) + abs(B_j - L_j) - 1

# if B, R, L are on the same row/col and R is in the middle of B and L
if (
  # same row
  B_i == R_i == L_i and (B_j < R_j < L_j or L_j < R_j < B_j)
  or
  # same col
  B_j == R_j == L_j and (B_i < R_i < L_i or L_i < R_i < B_i)
):
  distance += 2

# output
print(distance)



