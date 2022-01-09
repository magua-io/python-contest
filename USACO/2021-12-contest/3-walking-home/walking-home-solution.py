# Solution O(N^3):  there are O(N2) paths that Bessie can consider,
# and there are O(N) squares on each path to validate as being empty.

T = int(input())
for i in range(T):
  N, K = map(int, input().split())
  grid = []
  for i in range(N):
    grid.append(input())
  count = 0

  # If Bessie can only turn once, she must turn at either the top-right corner or the bottom-left corner.
  # Therefore, it suffices to check that the top row and right column are empty and that the bottom row and left column are empty.
  if K >= 1:
    top_right_path = True
    left_bottom_path = True
    for i in range(N):
      if grid[0][i] == 'H' or grid[i][N-1] == 'H':
        top_right_path = False
      if grid[i][0] == 'H' or grid[N-1][i] == 'H':
        left_bottom_path = False
    count += top_right_path + left_bottom_path

  # If Bessie is to make exactly two turns, then either she walks along the top row,
  # turns right and walks all the way to the bottom and then turns left,
  # or she walks along the left column, turns left, and walks all the way to the right and then turns right.
  # In the former case, we can brute force all columns Bessie would select.
  # In the latter case, we can brute force all rows Bessie would select.
  if K >= 2:
    # use column j to go down, not including rightmost column, which was included in K == 1 case.
    for j in range(1, N-1):
      valid = True
      for i in range(N):
        if grid[i][j] == 'H':
          valid = False
        # also check top row on the left of column j and bottom row on the right of column j
        if i < j and grid[0][i] == 'H':
          valid = False
        if i > j and grid[N-1][i] == 'H':
          valid = False
      count += valid

    # use row i to go right, not including bottom row,  which was included in K == 1 case.
    for i in range(1, N-1):
      valid = True
      for j in range(N):
        if grid[i][j] == 'H':
          valid = False
        # also check leftmost column above row i and rightmost column below row i
        if j < i and grid[j][0] == 'H':
          valid = False
        if j > i and grid[j][N-1] == 'H':
          valid = False
      count += valid

  # If Bessie is to make exactly three turns,
  # then Bessie ends up turning in the middle of the grid in some square
  # that is not in the top row, bottom row, left column, or right column.
  # We can brute force all inner squares that Bessie would select.
  if K >= 3:
    for i in range(1, N-1):
      for j in range(1, N-1):
        # RDRD
        valid = grid[i][j] == '.'
        for k in range(N):
          if k <= i and grid[k][j] == 'H':
            valid = False
          if k >= i and grid[k][N-1] == 'H':
            valid = False
          if k <= j and grid[0][k] == 'H':
            valid = False
          if k >= j and grid[i][k] == 'H':
            valid = False
        count += valid
        # DRDR
        valid = grid[i][j] == '.'
        for k in range(N):
          if k <= i and grid[k][0] == 'H':
            valid = False
          if k >= i and grid[k][j] == 'H':
            valid = False
          if k <= j and grid[i][k] == 'H':
            valid = False
          if k >= j and grid[N-1][k] == 'H':
            valid = False
        count += valid
  print(count)


# Solution 2: O(KN^2)
# We can also solve this problem in O(KN^2) time by storing for each square,
# each possible number of turns (up to K), and each of the directions D and R,
# the number of ways for Bessie to reach that square using exactly that number of turns
# such that the last direction in which she walked was that direction.
# However, this is outside of the scope of both Bronze and Silver.
