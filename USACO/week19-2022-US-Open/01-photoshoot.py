N = int(input())
cows = input()
res = 0
for i in range(N - 2, -1, -2):
    if (
        cows[i] == 'G' and cows[i + 1] == 'H' and res % 2 == 0
        or
        cows[i] == 'H' and cows[i + 1] == 'G' and res % 2 == 1
    ):
        res += 1
print(res)
