N = int(input())
locations = []
for _ in range(N):
    direction, location = input().split()
    locations.append((direction, int(location)))

res = N

for direction1, location1 in locations:
    count = 0
    for direction2, location2 in locations:
        if direction2 == 'G' and location1 < location2:
            count += 1
        elif direction2 == 'L' and location1 > location2:
            count += 1
    res = min(res, count)

print(res)
