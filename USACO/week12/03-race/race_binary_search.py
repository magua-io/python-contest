import sys

sys.stdin = open('race.in', 'r')
sys.stdout = open('race.out', 'w')


def test(distance, end_speed, peak_speed):
    dis = (peak_speed + 1) * peak_speed // 2
    if (peak_speed > end_speed):
        dis *= 2
        dis -= peak_speed
        dis -= (end_speed) * (end_speed - 1) // 2
    return dis <= distance


def min_time_spent(distance, end_speed):
    start = 1
    end = distance
    peak_speed = 0
    # use binary search to find the peak_speed
    while start + 1 < end:
        peak_speed = (start + end) // 2
        if (test(distance, end_speed, peak_speed)):
            start = peak_speed
        else:
            end = peak_speed

    peak_speed = start
    # inital total_time with time to reach peak speed
    total_time = start
    dis = (peak_speed + 1) * (peak_speed) // 2
    # symmetric distance on both side
    # but without peak_speed and from 1 to end_speed
    if peak_speed > end_speed:
        dis *= 2
        dis -= peak_speed
        # decrease the distance from 1 to (end_speed - 1)
        dis -= (1 + (end_speed - 1)) * (end_speed-1) // 2

        # add time needed to go back to end_speed
        total_time += peak_speed - end_speed

    remaining_distance = distance - dis

    # calculate how much longer can remain in peak_speed
    while (remaining_distance >= peak_speed):
        total_time += 1
        remaining_distance -= peak_speed

    if (remaining_distance == 0):
        return total_time
    else:
        # need another second to reach goal
        return total_time + 1


distance, n = map(int, input().split())
for _ in range(n):
    end_speed = int(input())
    print(min_time_spent(distance, end_speed))
