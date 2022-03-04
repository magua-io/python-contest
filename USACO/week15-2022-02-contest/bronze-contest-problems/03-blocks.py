N = int(input())
block1 = set(list(input()))
block2 = set(list(input()))
block3 = set(list(input()))
block4 = set(list(input()))

words = set()

combs = block1.union(block2, block3, block4)
blocks = [block1, block2, block3, block4]

for block in blocks:
    for c in block:
        word = [0] * 26
        word[ord(c) - ord('A')] += 1
        words.add(tuple(word))

for i in range(3):
    for j in range(i+1, 4):
        for a in blocks[i]:
            for b in blocks[j]:
                word = [0] * 26
                word[ord(a) - ord('A')] += 1
                word[ord(b) - ord('A')] += 1
                words.add(tuple(word))

for i in range(2):
    for j in range(i+1, 3):
        for k in range(j+1, 4):
            for a in blocks[i]:
                for b in blocks[j]:
                    for c in blocks[k]:
                        word = [0] * 26
                        word[ord(a) - ord('A')] += 1
                        word[ord(b) - ord('A')] += 1
                        word[ord(c) - ord('A')] += 1
                        words.add(tuple(word))

for a in block1:
    for b in block2:
        for c in block3:
            for d in block4:
                word = [0] * 26
                word[ord(a) - ord('A')] += 1
                word[ord(b) - ord('A')] += 1
                word[ord(c) - ord('A')] += 1
                word[ord(d) - ord('A')] += 1
                words.add(tuple(word))

for _ in range(N):
    word = input()
    word_list = [0] * 26
    for c in word:
        word_list[ord(c) - ord('A')] += 1
    if tuple(word_list) in words:
        print("YES")
    else:
        print("NO")
