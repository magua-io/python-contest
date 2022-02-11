import sys

sys.stdin = open('planting.in', 'r')
sys.stdout = open('planting.out', 'w')

# With n nodes and n - 1 edges, and all the nodes are connected.
# This is a tree.
# At most max(degrees) + 1 colors are needed.

n = int(input())
degrees = [0] * n
for _ in range(n - 1):
    a, b = map(int, input().split())
    degrees[a - 1] += 1
    degrees[b - 1] += 1
print(max(degrees) + 1)
