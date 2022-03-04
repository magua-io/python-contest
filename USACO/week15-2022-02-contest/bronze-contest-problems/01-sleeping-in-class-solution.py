def solve():
    N = int(input())
    sleeps = list(map(int, input().split()))
    total_sleeps = sum(sleeps)
    for r in range(N, 0, -1):
        if total_sleeps % r == 0:
            target_sum = total_sleeps // r
            cur_sum = 0
            ok = True
            for i in range(N):
                cur_sum += sleeps[i]
                if cur_sum > target_sum:
                    ok = False
                    break
                if cur_sum == target_sum:
                    cur_sum = 0
            if ok:
                print(N - r)
                return


T = int(input())
for _ in range(T):
    solve()
