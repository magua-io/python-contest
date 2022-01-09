g = [input() for i in range(8)]
d1 = [0] * 15
d2 = [0] * 15
c = [0] * 8
ans = 0

def dfs(r): # place queen in r-th row
	global ans
	if r == 8:
		ans += 1
	else:
		for i in range(8):
			if g[r][i] == '*':
				continue
			if c[i] or d1[r + i] or d2[i - r + 7]:
				continue
			c[i] = d1[r + i] = d2[i - r + 7] = 1
			dfs(r + 1)
			c[i] = d1[r + i] = d2[i - r + 7] = 0

dfs(0)
print(ans)