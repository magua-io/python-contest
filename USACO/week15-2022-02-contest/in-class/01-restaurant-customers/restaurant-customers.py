# Solution 1

n = int(input())
customers = []
for _ in range(n):
    start, end = map(int, input().split())
    customers.append([start, 1])
    customers.append([end + 1, -1])

customers.sort(key=lambda x: x[0])

sum = 0
max_sum = 0
for customer in customers:
    sum += customer[1]
    max_sum = max(max_sum, sum)

print(max_sum)


# Solution 2

n = int(input())
starts = []
ends = []
start_idx = 0
end_idx = 0

for _ in range(n):
    start, end = map(int, input().split())
    starts.append(start)
    ends.append(end)

starts.sort()
ends.sort()

cur = 0
max_sum = 0

while start_idx < n:
    if starts[start_idx] <= ends[end_idx]:
        cur += 1
        start_idx += 1
        max_sum = max(max_sum, cur)
    else:
        cur -= 1
        end_idx += 1

print(max_sum)
