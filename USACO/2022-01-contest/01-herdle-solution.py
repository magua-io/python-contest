correct = []
guess = []
for _ in range(3):
    correct += list(input())
for _ in range(3):
    guess += list(input())

green = 0
yellow = 0

freq_correct = [0] * 26
freq_guess = [0] * 26

for i in range(9):
    if correct[i] == guess[i]:
        green += 1
    freq_correct[ord(correct[i]) - ord('A')] += 1
    freq_guess[ord(guess[i]) - ord('A')] += 1

for i in range(26):
    yellow += min(freq_correct[i], freq_guess[i])
yellow -= green

print(green)
print(yellow)
