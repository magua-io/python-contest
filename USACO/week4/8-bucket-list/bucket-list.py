import sys

sys.stdin = open("blist.in", "r")
sys.stdout = open("blist.out", "w")

# Time complexity: O(N)

# read input
N = int(input())
milking_list = []
for _ in range(N):
  milking_list.append(list(map(int, input().split())))

# max Time is 1000, +1 due to 0-index
num_buckets_at_time = [0]*1001

# store the number of buckets needed at each time
for i in range(N):
  start, end, num_buckets = milking_list[i]
  num_buckets_at_time[start] += num_buckets
  num_buckets_at_time[end] -= num_buckets

max_buckets = 0
cur = 0
# iterate through each time and calculate
# the max number of buckets needed at some point
for num_bucket in num_buckets_at_time:
  cur += num_bucket
  max_buckets = max(max_buckets, cur)

print(max_buckets)
