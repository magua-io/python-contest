import sys

sys.stdin = open('lifeguards.in', 'r')
sys.stdout = open('lifeguards.out', 'w')

# Solution 1

n = int(input())
events = []

for i in range(n):
    start, end = map(int, input().split())
    events.append([start, i, 1])
    events.append([end, i, 0])

events.sort()

cows_alone_time = [0] * n
active_cows = set()
prev_time = 0
total_time = 0

for event in events:
    cur_time, cow_id, is_start_of_interval = event

    # update total time covered by all cows
    if len(active_cows) > 0:
        total_time += cur_time - prev_time

    # check if there is only one cow
    if len(active_cows) == 1:
        cows_alone_time[list(active_cows)[0]] += cur_time - prev_time

    # process the event
    if is_start_of_interval:
        active_cows.add(cow_id)
    else:
        active_cows.remove(cow_id)

    # update prev_time
    prev_time = cur_time

min_alone_time = min(cows_alone_time)

print(total_time - min_alone_time)


# Solution 2

n = int(input())
events = []

for _ in range(n):
    events.append(list(map(int, input().split())))

events.sort()

# total time covered by all cows (without duplication)
total_time = 0
prev_end = 0

for event in events:
    start, end = event
    if end > prev_end:
        # get the start time without overlapping
        start_without_overlap = max(prev_end, start)
        total_time += end - start_without_overlap
        prev_end = end

min_alone_time = total_time

# need to append the end of the last event as the start of the next event to avoid index out of range
events.append([events[n-1][1]])

prev_end = 0
for i in range(n):
    alone_time = max(
        0, min(events[i+1][0], events[i][1]) - max(events[i][0], prev_end))
    min_alone_time = min(min_alone_time, alone_time)
    prev_end = max(prev_end, events[i][1])

print(total_time - min_alone_time)
