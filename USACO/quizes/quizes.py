
# tuple quiz 1
# my_tuple = (1, 2, 3, 4)
# my_tuple.append((5, 6, 7))
# print(len(my_tuple))

# List quiz 1

# my_list = [1, 2, 3]
# my_list.append(5)
# my_list.pop()
# print(my_list)

# List quiz 2

# arr = [4, 2, 0, 0, 5]
# it = iter(arr)

# print(next(it), end=" ")
# print(next(it), end=" ")
# print(next(it))

arr1 = []
for i in range(2):
  for j in range(3):
    arr1.append([i, j])

arr2 = [[i, j] for i in range(2) for j in range(3)]
arr3 = [[i, j] for j in range(3) for i in range(2)]
arr4 = [[i, j] for i in range(3) for j in range(2)]
print("arr1:", arr1)
print("arr2:", arr2)
print("arr3:", arr3)
print("arr4:", arr4)
