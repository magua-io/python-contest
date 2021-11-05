# http://www.usaco.org/index.php?page=viewproblem2&cpid=567

with open('paint.in', 'r') as f:
  farmer_left, farmer_right = list(map(int, f.readline().split()))
  bessie_left, bessie_right = list(map(int, f.readline().split()))

with open('paint.out', 'w') as f:
  res = 0
  if bessie_right < farmer_left or bessie_left > farmer_right:
    res = bessie_right - bessie_left + farmer_right - farmer_left
  else:
    res = max(bessie_right, farmer_right) - min(bessie_left, farmer_left)
  f.write(str(res))