import sys
sys.stdin = open("square.in", "r")
sys.stdout = open("square.out", "w")

r1_x1, r1_y1, r1_x2, r1_y2 = list(map(int, input().split()))
r2_x1, r2_y1, r2_x2, r2_y2 = list(map(int, input().split()))

# find the coordinates of the smallest rectangle covering both pastures
bottom_left_x = min(r1_x1, r2_x1)
top_right_x = max(r1_x2, r2_x2)
bottom_left_y = min(r1_y1, r2_y1)
top_right_y = max(r1_y2, r2_y2)

# the smallest square will need a side length
# that is the maximum of the side lengths of the rectangle
side = max(top_right_x - bottom_left_x, top_right_y - bottom_left_y)
print(side * side)