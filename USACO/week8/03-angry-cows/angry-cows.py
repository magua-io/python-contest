import sys

sys.stdin = open('angry.in', 'r')
sys.stdout = open('angry.out', 'w')

# read input
N = int(input())
positions = []
for _ in range(N):
  positions.append(int(input()))

# sort hay bales so that easy to check left and right neighboring hay bales
positions.sort()

def get_max_num_hay_bales(start, direction):
  radius = 1
  prev = start

  while True:
    next_pos = prev
    while (
      0 <= next_pos + direction < N
      and radius >= abs(positions[next_pos + direction] - positions[prev])
    ):
      next_pos += direction

    if next_pos == prev:
      break

    # Update our previous explosion and increment radius
    prev = next_pos
    radius += 1

  return abs(prev - start)

max_num_hay_bales = 0
for i in range(N):
  max_num_hay_bales = max(
    max_num_hay_bales,
    get_max_num_hay_bales(i, -1) + 1 + get_max_num_hay_bales(i, 1)
  )

print(max_num_hay_bales)