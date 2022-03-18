import sys

sys.stdin = open('swap.in', 'r')
sys.stdout = open('swap.out', 'w')

N, K = map(int, input().split())
from1, to1 = map(int, input().split())
from2, to2 = map(int, input().split())
from1, to1 = from1 - 1, to1 - 1
from2, to2 = from2 - 1, to2 - 1

res = []
origin = []
for i in range(1, N+1):
    res.append(i)
    origin.append(i)

cycles_to_reset = 1
res[from1:to1+1] = res[from1:to1+1][::-1]
res[from2:to2+1] = res[from2:to2+1][::-1]

while res != origin:
    cycles_to_reset += 1
    res[from1:to1+1] = res[from1:to1+1][::-1]
    res[from2:to2+1] = res[from2:to2+1][::-1]

K %= cycles_to_reset
for _ in range(K):
    res[from1:to1+1] = res[from1:to1+1][::-1]
    res[from2:to2+1] = res[from2:to2+1][::-1]

for num in res:
    print(num)
