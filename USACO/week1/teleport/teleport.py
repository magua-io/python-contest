# http://www.usaco.org/index.php?page=viewproblem2&cpid=807

with open('teleport.in', 'r') as f1:
  a, b, x, y = list(map(int, f1.read().split()))
  option1 = abs(a - b)
  option2 = abs(a - x) + abs(b - y)
  option3 = abs(a - y) + abs(b - x)

with open('teleport.out', 'w') as f2:
  f2.write(str(min(option1, option2, option3)))