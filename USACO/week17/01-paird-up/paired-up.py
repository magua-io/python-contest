import sys

sys.stdin = open('pairup.in', 'r')
sys.stdout = open('pairup.out', 'w')

N = int(input())
all_cows = []
for _ in range(N):
    num_cows, milk_time = map(int, input().split())
    all_cows.append([milk_time, num_cows])

all_cows.sort()
left, right = 0, N - 1
max_time = 0

while left <= right:
    # how many cows have been grouped together.
    cows_to_milk = min(all_cows[left][1], all_cows[right][1])
    max_time = max(max_time, all_cows[left][0] + all_cows[right][0])
    if left == right:
        cows_to_milk /= 2
    all_cows[left][1] -= cows_to_milk
    all_cows[right][1] -= cows_to_milk
    # If there are no more cows which have this milk output,
    # we can increment/decrement the left/right pointer.
    if all_cows[left][1] == 0:
        left += 1
    if all_cows[right][1] == 0:
        right -= 1

print(max_time)
