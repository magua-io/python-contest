N = int(input())
initial_orders = list(map(int, input().split()))
final_orders = list(map(int, input().split()))

count = 0
i = N - 1
j = N - 1
removed = set()
while i >= 0:
    while final_orders and final_orders[j] in removed:
        j -= 1
    if initial_orders[i] != final_orders[j]:
        count += 1
        removed.add(initial_orders[i])
        i -= 1
    else:
        i -= 1
        j -= 1

print(count)
