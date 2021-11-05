# http://www.usaco.org/index.php?page=viewproblem2&cpid=591

with open('promote.in', 'r') as f:
  bronze_before, bronze_after = list(map(int, f.readline().split()))
  silver_before, silver_after = list(map(int, f.readline().split()))
  gold_before, gold_after = list(map(int, f.readline().split()))
  platinum_before, platinum_after = list(map(int, f.readline().split()))

with open('promote.out', 'w') as f:
  platinum_promoted = platinum_after - platinum_before
  gold_promoted = platinum_promoted + gold_after - gold_before
  silver_promoted = gold_promoted + silver_after - silver_before
  f.write(f'{silver_promoted}\n{gold_promoted}\n{platinum_promoted}')