import sys

sys.stdin = open('backforth.in', 'r')
sys.stdout = open('backforth.out', 'w')

# Solution 1: Naive way, list out all operations day by day

buckets_a = list(map(int, input().split()))
buckets_b = list(map(int, input().split()))

possible = set()

def friday(tank_a, buckets_a, buckets_b):
  for bucket in buckets_b:
    possible.add(tank_a + bucket)

def thursday(tank_a, buckets_a, buckets_b):
  for i, bucket in enumerate(buckets_a):
    new_buckets_b = buckets_b[:] + [bucket]
    new_buckets_a = buckets_a[:i] + buckets_a[i + 1:]
    friday(tank_a - bucket, new_buckets_a, new_buckets_b)

def wednesday(tank_a, buckets_a, buckets_b):
  for i, bucket in enumerate(buckets_b):
    new_buckets_a = buckets_a[:] + [bucket]
    new_buckets_b = buckets_b[:i] + buckets_b[i+1:]
    thursday(tank_a + bucket, new_buckets_a, new_buckets_b)

def tuesday(tank_a, buckets_a, buckets_b):
  for i, bucket in enumerate(buckets_a):
    new_buckets_b = buckets_b[:] + [bucket]
    new_buckets_a = buckets_a[:i] + buckets_a[i+1:]
    wednesday(tank_a - bucket, new_buckets_a, new_buckets_b)

tuesday(1000, buckets_a, buckets_b)

print(len(possible))


# Solution 2: better Recursive way, DRY (don't repeat yourself)

possible = set()

def transfer(day, tank_from, buckets_from, tank_to, buckets_to):
  # Last day, add the amount of milk in the first tank.
  if day == 4:
    possible.add(tank_from)
    return

  # This transfers every possible bucket from barn x to barn y.
  for i, bucket in enumerate(buckets_from):

    # Creates a new copy of available buckets, and transfers the ith one.
    # `new_buckets_from` now is `buckets_to + [bucket]`
    # `new_buckets_to` now is `buckets_from[:i] + buckets_from[i+1:]`
    new_buckets_from = buckets_to + [bucket]
    new_buckets_to = buckets_from[:i] + buckets_from[i+1:]

    new_tank_from = tank_to + bucket
    new_tank_to = tank_from - bucket

    # Recursively call the function with the new buckets and tank amounts.
    transfer(day + 1, new_tank_from, new_buckets_from, new_tank_to, new_buckets_to)

buckets_a = list(map(int, input().split()))
buckets_b = list(map(int, input().split()))

transfer(0, 1000, buckets_a, 1000, buckets_b)

print(len(possible))
