import sys

sys.stdin = open('sleepy.in', 'r')
sys.stdout = open('sleepy.out', 'w')

n = int(input())
cows = list(map(int, input().split()))

ans = 0

# Find the number of strictly increasing values at the end of the list
for i in range(n - 1, 0, -1):
    if cows[i] < cows[i - 1]:
        ans = i
        break

print(ans)
