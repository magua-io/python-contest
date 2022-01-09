# Solution 1: O(N^3)
# There are O(N^2) such substrings to check, and each one takes O(N) time to validate, for a total runtime of O(N^3).

N = int(input())
cows = input()
count = 0

for i in range(N):
  for j in range(i, N):
    # check substring(i, j)
    g = 0
    h = 0
    for k in range(i, j+1):
      if cows[k] == 'G':
        g += 1
      else:
        h += 1
    if g + h >= 3 and (g == 1 or h == 1):
      count += 1

print(count)


# Solution 2: O(N^2)
# To improve the performance of this solution, we can choose to check substrings in a specific order.
# In particular, fix the leftmost character in the substring and then start scanning to the right.
# If we have seen at least three characters and exactly one of them is G or one of them is H, increment a counter.
# Loop over all leftmost characters and then print the counter at the end. The approach of this solution is O(N^2).

N = int(input())
cows = input()
count = 0

for i in range(N):
  g = 0
  h = 0
  for j in range(i, N):
    if cows[j] == 'G':
      g += 1
    else:
      h += 1
    if g >= 2 and h >= 2:
      continue
    if g + h >= 3 and (g == 1 or h == 1):
      count += 1

print(count)


# Solution 3: O(N)
# For any letter that has different letter on its left or right,
# count the letters on the left and right that is different from itself separately
# increase `count` by `left * right + max(0, left-1) + max(0, right-1)`,
# where `left * right` is the number of lonely photos for cases like this "HHHGHH" or "GGGHGG",
# where `max(0, left-1)` is the number of lonely photos for cases like this "HHHG" or "GGGH",
# where `max(0, right-1)` is the number of lonely photos for cases like this "GHHH" or "HGGG".
# Although there are two loops in the algorithm, there will not be duplicate calculation.

N = int(input())
cows = input()
count = 0

for i in range(N):
  left = 0
  if i > 0 and cows[i-1] != cows[i]:
    left += 1
    k = i - 2
    while k >= 0 and cows[k] == cows[i-1]:
      left += 1
      k -= 1

  right = 0
  if i+1 < N and cows[i+1] != cows[i]:
    right += 1
    k = i + 2
    while k < N and cows[k] == cows[i+1]:
      right += 1
      k += 1

  count += left * right + max(0, left-1) + max(0, right-1)

print(count)

# Solution 4: O(N)
# Similar idea as Solution 3, but use some space to remember all the indices of each letter,
# so that no second loop needed. The number of letters on the left and right can be calculated
# by the difference between two indices

def calculate_lonely_photos(cows, N, cow):
  res = 0
  idxs = [-1]
  for i,c in enumerate(cows):
    if c == cow:
      idxs.append(i)
  idxs.append(N)

  for i in range(1, len(idxs)-1):
    left = idxs[i] - idxs[i-1] - 1
    right = idxs[i+1] - idxs[i] - 1

    res += max(0, left - 1)
    res += max(0, right - 1)

    if left > 0 and right > 0:
      res += left * right

  return res


N = int(input())
cows = input()
print(calculate_lonely_photos(cows, N, 'G') + calculate_lonely_photos(cows, N, 'H'))
