import sys

sys.stdin = open('factory.in', 'r')
sys.stdout = open('factory.out', 'w')

N = int(input())

outgoing = [0] * N
incoming = [0] * N
for _ in range(N - 1):
	a, b = map(int, input().split())
	# Counting number of outgoing and incoming walkways.
	outgoing[a-1] += 1
	incoming[b-1] += 1

res = -1
for i in range(N):
	# Found two meeting places. This won't work.
	# (we have to find a unique walkway)
	if outgoing[i] == 0 and res != -1: 
		res = -1
		break
	# Found a meeting place, save it.
	# (found a walkway which has only
	# has walkways leading into it.)
	if outgoing[i] == 0: 
		res = i + 1

print(res)