import sys

sys.stdin = open("lostcow.in", "r")
sys.stdout = open("lostcow.out", "w")

# read input
x, y = map(int, input().split())

# initialize variables
total_distance = 0
start = x
i = 0

while True:
	# We know that the sequence of x is [x+1, x-2, x+4, x-8, ...]
	# step is (-2)**i, where i starts from 0
	step = (-2) ** i
	# get next end location
	# Note: always starts from location x
	end = x + step
	# if from start to end John walks through y position, found Bessie!
	if (start < y <= end) or (start > y >= end):
		# calculate the new distance from y to start
		total_distance += abs(y - start)
		break
	else:
		# didn't walk through Bessie
		# calculate the new distance from end to start
		total_distance += abs(end - start)
	start = end
	# increase i
	i += 1

# output
print(total_distance)

