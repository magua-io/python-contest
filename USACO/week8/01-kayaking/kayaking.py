# read input
n = int(input())
weights = list(map(int, input().split()))

# sort weights list so that we can make sure
# that (weights[i+1] - weights[i]) is smaller, where i = 0, 2, 4, ..., 2n-2
weights.sort()

# minimum total instability, initialize with max positive infinity
min_total_instability = float('inf')

# iterate through weights, pick ith and jth weight for single kayaks,
# and calculate the
for i in range(2*n-1):
  for j in range(i+1, 2*n):
    # get the remaining weights by removing ith and jth weights
    remaining = weights[:i] + weights[i+1:j] + weights[j+1:]
    # calculate the total instability after removing ith and jth weights
    total_instability = 0
    for k in range(0, 2*n-2, 2):
      total_instability += remaining[k+1] - remaining[k]
    min_total_instability = min(min_total_instability, total_instability)

# output
print(min_total_instability)
