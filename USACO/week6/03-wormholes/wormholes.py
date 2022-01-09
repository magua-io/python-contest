import sys

sys.stdin = open('wormhole.in', 'r')
sys.stdout = open('wormhole.out', 'w')

# read input
N = int(input())
wormholes = [[0, 0]]
for _ in range(N):
  wormholes.append(list(map(int, input().split())))

# if wormhole j is the closest wormhole on the right of i,
# then next_on_right[i] = j
next_on_right = [0] * (N+1)

# if wormhole i and wormhole j is a pair,
# pairs[i] = j and pairs[j] = i
pairs = [0] * (N+1)

# get all next on right for every wormholes
for i in range(1, N+1):
  for j in range(1, N+1):
    if i == j:
      continue
    x_i, y_i = wormholes[i]
    x_j, y_j = wormholes[j]
    # wormhole j is on the right of wormhole i
    if x_j > x_i and y_j == y_i:
      # only update next_on_right[i] = j when there is not next_on_right value yet
      # or the wormhole j is closer to wormhole i compared to previously set wormhole next_on_right[i]
      if next_on_right[i] == 0 or x_j < wormholes[next_on_right[i]][0]:
        next_on_right[i] = j

def cycle_exists():
  # check every wormhole to start with
  # if after N steps, the pos is still not 0,
  # it means that there is a infinite cycle
  for start in range(1, N+1):
    pos = start
    for _ in range(N):
      pos = next_on_right[pairs[pos]]
    if pos != 0:
      return True
  return False

def find_wormhole_pairs_that_cause_infinite_cycle():
  # the count of possible distinct pairing of wormholes that cause infinite cycle
  count = 0
  # find first unpaired wormhole
  wormhole_idx = 0
  for i in range(1, N+1):
    if pairs[i] == 0:
      wormhole_idx = i
      break

  # every wormholes are paired
  if wormhole_idx == 0:
    # check cycles
    return 1 if cycle_exists() else 0

  # try to pair wormholes[wormhole_idx] with all other wormholes
  for i in range(wormhole_idx+1, N+1):
    # wormhole at index i is not paired yet
    if pairs[i] == 0:
      pairs[i] = wormhole_idx
      pairs[wormhole_idx] = i
      count += find_wormhole_pairs_that_cause_infinite_cycle()
      # unpair current pair for next iteration
      pairs[i] = pairs[wormhole_idx] = 0

  return count

print(find_wormhole_pairs_that_cause_infinite_cycle())