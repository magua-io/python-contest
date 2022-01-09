# import sys
# import heapq
# sys.stdin = open("shortcut.in", "r")
# sys.stdout = open("shortcut.out", "w")
#
# MAX_N = 10005
# # State: [vertex, distance]
#
# # Edge: [other_vertex, weight]
#
# parents = [-1]*MAX_N
# cows = [0]*MAX_N
# # shortest distance from vertex 1
# djik = [sys.maxsize]*MAX_N
# djik[1] = 0
# # number of cows that pass through that vertex
# nums = [0]*MAX_N
#
# N, M, T = map(int, input().split())
# cows = []
# cows = list(map(int, input().split()))
# cows = [0] + cows
#
#
#
# # edge list
# edge_list = [[] for _ in range(N+1)]
# for _ in range(M):
#   a, b, t = map(int, input().split())
#   edge_list[a].append([b, t])
#   edge_list[b].append([a, t])
#
# max_heap = []
# count = 0
# # heap entry (negative distance, count, field)
# heapq.heappush(max_heap, (sys.maxsize, 0, 1))
# count += 1
#
# seen = set()
# seen.add(1)
#
# while max_heap:
#   from_vertex = heapq.heappop(max_heap)
#   distance, count, from_vertex_field = from_vertex
#
#   seen.add(from_vertex_field)
#
#   for edge in edge_list[from_vertex_field]:
#     to_vertex, weight = edge
#     if to_vertex in seen:
#       continue
#     new_distance = djik[from_vertex_field] + weight
#     if (
#         new_distance < djik[to_vertex] or
#         # ensures lexicographically shortest path
#         new_distance == djik[to_vertex] and from_vertex_field < parents[to_vertex]
#     ):
#       djik[to_vertex] = new_distance
#       parents[to_vertex] = from_vertex_field
#       heapq.heappush(max_heap, (new_distance, count, to_vertex))
#       count += 1
#
# for k in range(1, N+1):
#   # backtrack to fill nums
#   i = k
#   while i != -1:
#     nums[i] += cows[k]
#     i = parents[i]
#
# answer = 0
# for k in range(1, N+1):
#   # nums[k] * (djik[k] - t) is the distance saved
#   answer = max(answer, nums[k] * (djik[k] - T))
#
# print(answer)



# Solution 2

import sys
import heapq

sys.setrecursionlimit(20000)

sys.stdin = open("shortcut.in", "r")
sys.stdout = open("shortcut.out", "w")

MAX_N = 10005
# State: [vertex, distance]

# Edge: [other_vertex, weight]

parents = [-1] * MAX_N
cows = [0] * MAX_N
# shortest distance from vertex 1
djik = [sys.maxsize] * MAX_N
djik[1] = 0
# number of cows that pass through that vertex
nums = [0] * MAX_N

edge_list_for_shortest_path_tree = [[] for _ in range(MAX_N)]


def dfs(v, p):
  sum = cows[v]
  for nei in edge_list_for_shortest_path_tree[v]:
    if nei == p:
      continue
    dfs(nei, v)
    sum += nums[nei]

  nums[v] = sum


N, M, T = map(int, input().split())
cows = []
cows = list(map(int, input().split()))
cows = [0] + cows

# edge list
edge_list = [[] for _ in range(N + 1)]
for _ in range(M):
  a, b, t = map(int, input().split())
  edge_list[a].append([b, t])
  edge_list[b].append([a, t])

max_heap = []
count = 0
# heap entry (negative distance, count, field)
heapq.heappush(max_heap, (sys.maxsize, 0, 1))
count += 1

seen = set()
seen.add(1)

while max_heap:
  from_vertex = heapq.heappop(max_heap)
  distance, count, from_vertex_field = from_vertex

  seen.add(from_vertex_field)

  for edge in edge_list[from_vertex_field]:
    to_vertex, weight = edge
    if to_vertex in seen:
      continue
    new_distance = djik[from_vertex_field] + weight
    if (
        new_distance < djik[to_vertex] or
        # ensures lexicographically shortest path
        new_distance == djik[to_vertex] and from_vertex_field < parents[to_vertex]
    ):
      djik[to_vertex] = new_distance
      parents[to_vertex] = from_vertex_field
      heapq.heappush(max_heap, (new_distance, count, to_vertex))
      count += 1

for k in range(2, N+1):
  edge_list_for_shortest_path_tree[k].append(parents[k])
  edge_list_for_shortest_path_tree[parents[k]].append(k)

dfs(1, -1)

answer = 0
for k in range(1, N + 1):
  # nums[k] * (djik[k] - t) is the distance saved
  answer = max(answer, nums[k] * (djik[k] - T))

print(answer)