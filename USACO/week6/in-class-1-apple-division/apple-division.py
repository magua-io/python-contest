n = int(input())
p = list(map(int, input().split()))

def solve(i, s1, s2):
	if i == n:
		return abs(s2 - s1)
	return min(solve(i + 1, s1 + p[i], s2),
			   solve(i + 1, s1, s2 + p[i]))

print(solve(0, 0, 0))