from collections import defaultdict
import sys

sys.stdin = open('badmilk.in', 'r')
sys.stdout = open('badmilk.out', 'w')

N, M, D, S = map(int, input().split())
person_to_milk = defaultdict(list)
milk_to_person = defaultdict(set)

# read input and store information in data structure
for _ in range(D):
    person, milk, time = map(int, input().split())
    if len(person_to_milk[person]) == 0:
        person_to_milk[person] = [[] for _ in range(101)]
    person_to_milk[person][time].append(milk)
    milk_to_person[milk].add(person)

# get all possible bad milk
possible_bad_milks = []
for _ in range(S):
    person, time = map(int, input().split())
    bad_milk_set = set()
    for t in range(1, time):
        bad_milk_set = bad_milk_set.union(set(person_to_milk[person][t]))
    possible_bad_milks.append(bad_milk_set)

possible_bad_milks_set = set.intersection(*possible_bad_milks)

# get maximum doses needed
max_doses = 0
for milk in possible_bad_milks_set:
    max_doses = max(max_doses, len(milk_to_person[milk]))

print(max_doses)
