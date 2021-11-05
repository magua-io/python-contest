with open('mountain-climbing.in', 'r') as f:
  N = int(f.readline())
  mountains = list(map(int, f.readline().split()))

with open('mountain-climbing.out', 'w') as f:
  res = 0
  if N == 1:
    res = mountains[0] * 2 + 1
  else:
    res = mountains[0] + mountains[-1] + N
    for i, h in enumerate(mountains):
      if i == 0:
        continue
      else:
        res += abs(h - mountains[i-1])
  f.write(str(res))


