import sys

sys.stdin = open('milkorder.in', 'r')
sys.stdout = open('milkorder.out', 'w')

"""
In this problem, there are three cases that we have to consider:

1. ow 1 is fixed: In this case, the solution is simple, as we just output its fixed position.
2. Cow 1 is in the given hierarchy of cows: In this case, we want to place every cow in the hierarchy as early as possible.
3. Cow 1 is neither fixed nor in the hierarchy: In this case, we would want to place every cow in the hierarchy as late as possible, such that cow 1 gets the earliest possible position.
"""

N, M, K = map(int, input().split())
hierarchy = list(map(int, input().split()))
fixed = [list(map(int, input().split())) for _ in range(K)]

cows = [0] * N

for i in range(K):
    cows[fixed[i][1] - 1] = fixed[i][0]

if 1 in cows:
    # Case 1
    ans = cows.index(1) + 1
else:
    if 1 in hierarchy:
        # Case 2, cow 1 in hierarchy, fill hierarchy from start to the end
        i = 0
        pointer = 0
        while pointer < M:
            if hierarchy[pointer] in cows:
                i = cows.index(hierarchy[pointer]) + 1
                pointer += 1
            else:
                while cows[i] != 0:
                    i += 1
                cows[i] = hierarchy[pointer]
                i += 1
                pointer += 1
        for i in range(N):
            if cows[i] == 1:
                ans = i + 1
                break
    else:
        # Case 3, cow 1 not in hierarchy, fill hierarchy from the end to the start
        i = N - 1
        pointer = M - 1
        while pointer >= 0:
            if hierarchy[pointer] in cows:
                i = cows.index(hierarchy[pointer]) - 1
                pointer -= 1
            else:
                if cows[i] == 0:
                    cows[i] = hierarchy[pointer]
                    i -= 1
                    pointer -= 1
                else:
                    i -= 1

        for i in range(N):
            if cows[i] == 0:
                ans = i + 1
                break

print(ans)
