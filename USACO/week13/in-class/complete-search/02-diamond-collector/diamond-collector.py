import sys

sys.stdin = open('diamond.in', 'r')
sys.stdout = open('diamond.out', 'w')


N, K = map(int, input().split())

diamonds = []

for _ in range(N):
	diamonds.append(int(input()))

largest = 0
curlargest = 0
for x in range(N):
	for y in range(N):
		if diamonds[y] >= diamonds[x] and diamonds[y] <= diamonds[x] + K:
			curlargest += 1
	largest = max(largest, curlargest)
	curlargest = 0

print(largest)