T = int(input())
for _ in range(T):
    N = int(input())
    sleeps = list(map(int, input().split()))

    total_sleeps = sum(sleeps)
    min_sleep = min(sleeps)
    max_sleep = max(sleeps)
    if min_sleep == max_sleep:
        print(0)
        continue

    n = N
    should_break = False
    while not should_break:
        if total_sleeps % n == 0:
            final_sleep = total_sleeps // n
            count = 0
            total_count = 0
            new_sleeps = []
            i = 0
            cur_sleep = 0
            while i < N:
                if cur_sleep != final_sleep:
                    count += 1
                    cur_sleep += sleeps[i]
                    if cur_sleep > final_sleep:
                        break
                    elif cur_sleep == final_sleep:
                        new_sleeps.append(final_sleep)
                        cur_sleep = 0
                        total_count += count - 1
                        count = 0
                i += 1
                if i == N:
                    print(total_count)
                    should_break = True

        n -= 1
