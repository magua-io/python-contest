import sys

sys.stdin = open("shuffle.in", "r")
sys.stdout = open("shuffle.out", "w")

# read inputs
N = int(input())
shuffle_orders = list(map(int, input().split()))
ids = list(map(int, input().split()))

# helper function to shuffle
def shuffle(ids, shuffle_orders):
  # new ids
  new_ids = []
  # shuffle
  for i in shuffle_orders:
    # remember to change shuffle orders to 0-based index by minus 1
    new_ids.append(ids[i-1])
  return new_ids

def shuffle2(ids, shuffle_orders):
  after = ids[:]
  before = ids[:]
  for i in range(len(ids)):
    after[shuffle_orders[i]-1] = ids[i]
    before[i] = ids[shuffle_orders[i]-1]
  print("after:", after)
  print("before:", before)
  return before

# shuffle 3 times
for _ in range(3):
  ids = shuffle2(ids, shuffle_orders)
  print(ids)

# output
for id in ids:
  print(id)
