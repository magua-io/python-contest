import sys

sys.stdin = open('rental.in', 'r')
sys.stdout = open('rental.out', 'w')

# key observations
# 1. we want to sell to shops that pay more per gallon of milk over shops that pay less per gallon of milk.
# 2. we want to rent cows that produce less milk over cows that produce more milk.
#
# We can use f(i) to represents the max profit of selling first i cows's milk
# We can use g(n-i) to represents the max profit of leasing last (n-i) cows.
# max_profits(i) = f(i) + g(n-i), represents selling the milk of first i cows and leasing the rest of cows
# after calculating max_profits for [0, n], then we can get the max profit with max(max_profits)

N, M, R = map(int, input().split())
milk_production = []
milk_buy = []
cow_rental = []

for _ in range(N):
    milk_production.append(int(input()))
for _ in range(M):
    milk_buy.append(list(map(int, input().split())))
for _ in range(R):
    cow_rental.append(int(input()))

milk_production.sort(reverse=True)
milk_buy.sort(key=lambda x: -x[1])
cow_rental.sort(reverse=True)

# calculating the max profit of selling the milk of first i cows (prefix sum)
max_profits = [0] * (N + 1)
buy_milk_index = 0
for i in range(N):
    max_profits[i+1] = max_profits[i]
    while buy_milk_index < M and milk_production[i] > 0:
        milk_to_sell = min(milk_production[i], milk_buy[buy_milk_index][0])
        max_profits[i+1] += milk_to_sell * milk_buy[buy_milk_index][1]
        milk_production[i] -= milk_to_sell
        milk_buy[buy_milk_index][0] -= milk_to_sell
        if milk_buy[buy_milk_index][0] == 0:
            buy_milk_index += 1

# calculating the max profit by adding the profit of leasing (n-i) cows (prefix sum as well)
rent_index = 0
index = N - 1
rent_profit_sum = 0
while index >= 0 and rent_index < R:
    rent_profit_sum += cow_rental[rent_index]
    max_profits[index] += rent_profit_sum
    rent_index += 1
    index -= 1

# get max profit
print(max(max_profits))
