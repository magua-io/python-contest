import sys

sys.stdin = open('mixmilk.in', 'r')
sys.stdout = open('mixmilk.out', 'w')

N = 3
capacity = [0]*N
milk = [0]*N

def pour(i, j):
  amount = min(milk[i], capacity[j]-milk[j])
  milk[i] -= amount
  milk[j] += amount

for i in range(N):
  capacity[i], milk[i] = map(int, input().split())
for i in range(100):
  pour(i%N, (i+1)%N)
for i in range(N):
  print(milk[i])


