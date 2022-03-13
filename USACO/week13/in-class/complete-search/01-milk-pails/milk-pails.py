import sys

sys.stdin = open('pails.in', 'r')
sys.stdout = open('pails.out', 'w')

buck1, buck2, buck3 = map(int, input().split())

ans = 0

# x and y below take care of all
# possible combinations of the two buckets.

for x in range(1001):
	if (buck1 * x) > buck3:
		break
	for y in range(1001):
		current = (buck1 * x) + (buck2 * y)
		if current > buck3:
			break
		ans = max(ans, current)

print(ans)
