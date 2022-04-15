from collections import defaultdict


N = int(input())


def get_metal(i, metals, recipes):
    metal_to = i
    metals_from = recipes.get(metal_to)
    if metals_from == None:
        return False
    for metal in metals_from:
        if metals[metal] > 0:
            metals[metal] -= 1
        else:
            if not get_metal(metal, metals, recipes):
                return False
    return True


metals = [0] + list(map(int, input().split()))
K = int(input())
recipes = defaultdict(list)
for _ in range(K):
    recipe = list(map(int, input().split()))
    recipes[recipe[0]] = recipe[2:]

count = metals[N]
while get_metal(N, metals, recipes):
    count += 1

print(count)
