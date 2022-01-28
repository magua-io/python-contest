import sys

sys.stdin = open('notlast.in', 'r')
sys.stdout = open('notlast.out', 'w')

N = int(input())
cows = ['Bessie', 'Elsie', 'Daisy', 'Gertie', 'Annabelle', 'Maggie', 'Henrietta']
cow_milk_dict = {}
for cow in cows:
  cow_milk_dict[cow] = 0

for _ in range(N):
  line = input().split()
  cow = line[0]
  milk = int(line[1])
  cow_milk_dict[cow] += milk

min_milk = 100 * N
min_cow = ''
second_min_milk = 100 * N
second_min_cow = ''
second_min_cow_count = 0

# generate {cow: milk} dictionary
for cow, milk in cow_milk_dict.items():
  if milk < min_milk:
    min_milk = milk
    min_cow = cow

# get minimum milk and corresponding cow
for cow, milk in cow_milk_dict.items():
  if min_milk < milk < second_min_milk:
    second_min_milk = milk
    second_min_cow = cow

# get second minimum milk and corresponding cow
for cow, milk in cow_milk_dict.items():
  if milk == second_min_milk:
    second_min_cow_count += 1

# if more than 1 second minimum cow found or no second minimum cow found
if second_min_cow_count > 1 or second_min_cow == '':
  print('Tie')
  exit()

print(second_min_cow)