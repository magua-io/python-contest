s = input()
perms = []
char_count = [0] * 26

# Solution 1
def search(curr):
	# we've finished creating a permutation
	if len(curr) == len(s):
		perms.append(curr)
		return
	for i in range(26):
		# for all available characters
		if char_count[i] > 0:
			# add it to the current string and search
			char_count[i] -= 1
			search(curr + chr(ord('a') + i))
			char_count[i] += 1

for c in s:
	char_count[ord(c) - ord('a')] += 1

search("")
print(len(perms))
for perm in perms:
	print(perm)


# Solution 2
import itertools
s = input()
# perms is a sorted list of all the permutations of the given string
perms = sorted(set(itertools.permutations(s)))
print(len(perms))
for perm in perms:
	print("".join(perm))