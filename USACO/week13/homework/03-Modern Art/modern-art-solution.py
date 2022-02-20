import sys

sys.stdin = open('art.in', 'r')
sys.stdout = open('art.out', 'w')

n = int(input().strip())
grid = [[int(i) for i in input()] for _ in range(n)]

# rect[color] = [x1, y1, x2, y2]
# where (x1, y1) is the top left corner of the rectangle
# and (x2, y2) is the bottom right corner of the rectangle
rect = []
for _ in range(10):
    rect.append([n, n, -1, -1])

# Find out rect for each color
for i in range(n):
    for j in range(n):
        a = grid[i][j]
        # the cell has been filled with some color
        if a > 0:
            rect[a][0] = min(rect[a][0], i)
            rect[a][1] = min(rect[a][1], j)
            rect[a][2] = max(rect[a][2], i)
            rect[a][3] = max(rect[a][3], j)

ans = 0
not_original = [0]*10
for color in range(10):
    # if color is visible on the canvas
    if rect[color][0] < n:
        ans = ans + 1
        # any color inside another rect cannot be original color
        for i in range(rect[color][0], rect[color][2]+1):
            for j in range(rect[color][1], rect[color][3]+1):
                if grid[i][j] != color:
                    not_original[grid[i][j]] = 1

print(ans - sum(not_original))
