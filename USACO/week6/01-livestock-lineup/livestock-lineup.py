import sys

sys.stdin = open('lineup.in', 'r')
sys.stdout = open('lineup.out', 'w')

# Solution 1: Brute force that tries all ordering

import itertools

N = int(input())
cows = ['Beatrice', 'Belinda', 'Bella', 'Bessie', 'Betsy', 'Blue', 'Buttercup', 'Sue']
constraints = []

for _ in range(N):
  cur = input().split()
  constraints.append([cur[0], cur[-1]])
  constraints.append([cur[-1], cur[0]])

permutations = list(itertools.permutations(cows))

for permutation in permutations:
  meet_constraint_num = 0
  for constraint in constraints:
    if (
      permutation.index(constraint[0])+1 == permutation.index(constraint[1])
      or permutation.index(constraint[0])-1 == permutation.index(constraint[1])
    ):
      meet_constraint_num += 1
  if meet_constraint_num == len(constraints):
    for cow in permutation:
      print(cow)
    exit()

# Solution 2: more analytical one that tries to build up the alphabetically first ordering one cow at a time.

# number of constraints
N = int(input())
# already sorted alphabetically
cows = ['Beatrice', 'Belinda', 'Bella', 'Bessie', 'Betsy', 'Blue', 'Buttercup', 'Sue']
# constraints[i][0] represents the cow at the beginning of the constraint
# constraints[i][1] represents the cow at the end of the constraint
# e.g. for constraint "Buttercup must be milked beside Bella",
# where constraints[i][0] is "Buttercup", and constraints[i][1] is "Bella".
constraints = []
# list that stores final order of cows
result = []
# cows that have been lined up
arranged_cows = set()

# read all constraints
for _ in range(N):
  cur = input().split()
  constraints.append([cur[0], cur[-1]])

# whether the provided cow can go next
def can_go_next(cow):
  arranged_cows_num = len(result)
  num_neighbors = 0
  # the cow has been arranged
  if cow in arranged_cows:
    return False

  # check constraints and find how many neighbors the cow has
  for constraint in constraints:
    if constraint[0] == cow and constraint[1] not in arranged_cows:
      num_neighbors += 1
    if constraint[1] == cow and constraint[0] not in arranged_cows:
      num_neighbors += 1

  # if the cow has 2 neighbors, it means that one of its neighbors should go next
  if num_neighbors == 2:
    return False

  # check whether previously arranged cow has constraint
  if arranged_cows_num > 0:
    prev_cow = result[-1]
    # if prev_cow has neighbor and it is not the cow, return False
    for constraint in constraints:
      if (
        constraint[0] == prev_cow
        and constraint[1] not in arranged_cows
        and constraint[1] != cow
      ):
        return False
      if (
          constraint[1] == prev_cow
          and constraint[0] not in arranged_cows
          and constraint[0] != cow
      ):
        return False

  return True

# Iterate 8 times, line up one cow per iteration.
for i in range(8):
  next_cow = 0
  # skipping all the cows that cannot go next
  while not can_go_next(cows[next_cow]):
    next_cow += 1
  # add lined up cow to the result list
  result.append(cows[next_cow])
  # add lined up cow to `arranged_cows` set
  arranged_cows.add(cows[next_cow])
  # print the lined up cow
  print(cows[next_cow])


