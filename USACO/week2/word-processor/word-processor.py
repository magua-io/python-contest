# read input
with open('word.in', 'r') as fin:
  lines = fin.readlines()
  N, K = list(map(int, lines[0].split()))
  arr = lines[1].split()

# print output
with open('word.out', 'w') as fout:
  # number of characters in current line, excluding spaces
  count = 0
  # current line of words
  line = []
  # iterate words
  for word in arr:
    # if next word + existing words can fit in the current line
    if count + len(word) <= K:
      line.append(word)
    else:
      # write the previous line
      fout.write(f"{' '.join(line)}\n")
      # reset count
      count = 0
      # reset line
      line.clear()
      line.append(word)
    # increase word count in the current line
    count += len(word)

  # if no remaining words but
  if count > 0:
    fout.write(f"{' '.join(line)}\n")
