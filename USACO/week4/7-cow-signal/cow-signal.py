import sys

sys.stdin = open("cowsignal.in", "r")
sys.stdout = open("cowsignal.out", "w")

# My Solution:

# read input
M, N, K = map(int, input().split())
signal = []
for _ in range(M):
  signal.append(input())

enlarged_signal = []

for idx,row in enumerate(signal):
  new_row = []
  # for each element, repeat K times in the enlarged signal
  for i in range(N):
    for _ in range(K):
      new_row.append(signal[idx][i])
  # for each line, repeat K times in the enlarged signal
  for _ in range(K):
    enlarged_signal.append(new_row)

# output, join the list with empty string
for line in enlarged_signal:
  print(''.join(line))


# Official Solution:

M,N,K = map(int,input().split())
g = [input() for _ in range(M)]
for i in range(K*M):
	for j in range(K*N):
		print(g[i//K][j//K], end='')
	print()