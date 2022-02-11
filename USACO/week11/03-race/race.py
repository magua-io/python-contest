import sys

sys.stdin = open('race.in', 'r')
sys.stdout = open('race.out', 'w')


def min_time_spent(distance, end_speed):
    # distance travelled when increasing speed
    lhstravel = 0
    # distance travelled when reducing speed
    rhstravel = 0
    timeused = 0
    # speed always start with 1
    currspeed = 1
    while True:
        lhstravel += currspeed
        timeused += 1
        # when total distance >= provide distance, return timeused
        if lhstravel + rhstravel >= distance:
            return timeused
        # if current speed is >= end_speed
        # currspeed is not peak, you need to travel this speed at least twice
        # once in lhstravel, and the other in rhstravel
        # For example,
        # K = 15, X = 2
        # 1, 2, 3, 4, 3, 2 (optimal solution),
        # peak speed only travels 1 min,
        # other speed that >= end_speed travel twice
        if currspeed >= end_speed:
            rhstravel += currspeed
            timeused += 1
            if lhstravel + rhstravel >= distance:
                return timeused
        currspeed += 1


K, N = map(int, input().split())
for _ in range(N):
    X = int(input())
    print(min_time_spent(K, X))
