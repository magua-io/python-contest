import sys

sys.stdin = open('tracing.in', 'r')
sys.stdout = open('tracing.out', 'w')

# read inputs
N, T = map(int, input().split())
ill_cows = set()
state = input()
for i in range(N):
    if state[i] == '1':
        # add 1 becaused cow is represents with 1-index based
        ill_cows.add(i + 1)

events = []
for _ in range(T):
    events.append(list(map(int, input().split())))

# sort events so that we can iterate through events based on the correct timeline
events.sort()

x = y = z = 0
# use set to keep track of valid pation zeros
valid_pation_zeros = set()
min_k = N
max_k = 0

# try to find the max number of contacts that some cow has
# so that we can use it as max_k when iterating
contacts = [0] * N
for _, cow_from, cow_to in events:
    contacts[cow_from - 1] += 1
    contacts[cow_to - 1] += 1
max_contacts = max(contacts)

# try every current ill cow as patient zero and see whether it can reach same ill cows state
for patient_zero in ill_cows:
    # try different values of k and see whether it can reach same ill cows state
    for k in range(max_contacts + 1):
        patient_count = 1
        cur_ill_cows = set([patient_zero])
        # use dict to keep track of how many times the cow can still spread the disease
        ill_cow_to_k_dict = {patient_zero: k}

        # iterate through events
        for _, cow_from, cow_to in events:
            # decrease the number of remaining spreads if needed
            if cow_from in ill_cow_to_k_dict:
                ill_cow_to_k_dict[cow_from] -= 1
            if cow_to in ill_cow_to_k_dict:
                ill_cow_to_k_dict[cow_to] -= 1

            # successfully spread the disease to not ill cow
            if cow_from in cur_ill_cows and cow_to not in cur_ill_cows and ill_cow_to_k_dict[cow_from] >= 0:
                cur_ill_cows.add(cow_to)
                ill_cow_to_k_dict[cow_to] = k
            elif cow_to in cur_ill_cows and cow_from not in cur_ill_cows and ill_cow_to_k_dict[cow_to] >= 0:
                cur_ill_cows.add(cow_from)
                ill_cow_to_k_dict[cow_from] = k

        # if the final state is the same as current state,
        # it means that the selected patient zero and selected k value can reach same ill cows state
        if cur_ill_cows == ill_cows:
            valid_pation_zeros.add(patient_zero)
            min_k = min(min_k, k)
            max_k = max(max_k, k)

# if max_k is the same as max_contacts, then, k can be infinity
if max_k == max_contacts:
    print(len(valid_pation_zeros), min_k, 'Infinity')
else:
    print(len(valid_pation_zeros), min_k, max(max_k, min_k))
