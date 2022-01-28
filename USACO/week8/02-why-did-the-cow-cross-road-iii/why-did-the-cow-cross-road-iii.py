import sys

sys.stdin = open('cowqueue.in', 'r')
sys.stdout = open('cowqueue.out', 'w')

# read input
N = int(input())
cows = []
for _ in range(N):
  entry_time, process_time = map(int, input().split())
  # cows[i] represents [entry_time, process_time]
  cows.append([entry_time, process_time])

# sort the cows based on entry_time
cows.sort(key=lambda x: x[0])

cur_time = 0
for cow in cows:
  # if cow arrives earlier than current time,
  # just need to add the process time to current time
  if cur_time > cow[0]:
    cur_time += cow[1]
  # if cow arrives later than current time,
  # just need to set current time to entry_time + process_time
  else:
    cur_time = cow[0] + cow[1]

print(cur_time)
