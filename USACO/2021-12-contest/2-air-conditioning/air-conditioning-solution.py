# Solution 1: O(N * V), where V is the maximum possible value in d. Under the given bounds though,
# the answer can be as large as one billion, so we need to do better than simulating this step by step.

N = int(input())
preferred_temperatures = list(map(int, input().split()))
actual_temperatures = list(map(int, input().split()))

diff_temperatures = [0]*N
for i in range(N):
  diff_temperatures[i] = preferred_temperatures[i] - actual_temperatures[i]

totalOperations = 0

while diff_temperatures:
  if diff_temperatures[-1] == 0:
    diff_temperatures.pop()
    continue

  is_positive = diff_temperatures[-1] > 0
  amt_change = 1

  while  amt_change < len(diff_temperatures):
    if diff_temperatures[-1 - amt_change] == 0:
      break
    if (diff_temperatures[-1 - amt_change] > 0) != is_positive:
      break
    amt_change += 1

  totalOperations += 1

  for i in range(amt_change):
    if diff_temperatures[-1 - i] > 0:
      diff_temperatures[-1-i] -= 1
    else:
      diff_temperatures[-1 - i] += 1

print(totalOperations)


# Solution 2: O(N * V), One thing worth trying that does pass all test cases is,
# instead of just incrementing or decrementing by one,
# doing as many increments/decrements as possible until some element becomes zero.

N = int(input())
preferred_temperatures = list(map(int, input().split()))
actual_temperatures = list(map(int, input().split()))

diff_temperatures = [0]*N
for i in range(N):
  diff_temperatures[i] = preferred_temperatures[i] - actual_temperatures[i]

totalOperations = 0

while diff_temperatures:
  if diff_temperatures[-1] == 0:
    diff_temperatures.pop()
    continue

  is_positive = diff_temperatures[-1] > 0
  amt_change = 1
  delta = abs(diff_temperatures[-1])

  while  amt_change < len(diff_temperatures):
    if diff_temperatures[-1 - amt_change] == 0:
      break
    if (diff_temperatures[-1 - amt_change] > 0) != is_positive:
      break
    delta = min(delta, abs(diff_temperatures[-1 - amt_change]))
    amt_change += 1

  totalOperations += delta

  for i in range(amt_change):
    if diff_temperatures[-1 - i] > 0:
      diff_temperatures[-1-i] -= delta
    else:
      diff_temperatures[-1 - i] += delta

print(totalOperations)