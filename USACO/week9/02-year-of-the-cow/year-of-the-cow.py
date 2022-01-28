N = int(input())

zodiac_dict = {
  'Ox': 0,
  'Tiger': 1,
  'Rabbit': 2,
  'Dragon': 3,
  'Snake': 4,
  'Horse': 5,
  'Goat': 6,
  'Monkey': 7,
  'Rooster': 8,
  'Dog': 9,
  'Pig': 10,
  'Rat': 11,
}

cow_age_map = {
  'Bessie': 0,
}

cow_zodiac_map = {
  'Bessie': 'Ox',
}

for _ in range(N):
  line = input().split()
  new_cow = line[0]
  is_previous = line[3] == 'previous'
  zodiac = line[4]
  mentioned_cow = line[-1]

  cow_zodiac_map[new_cow] = zodiac

  if is_previous:
    # get diff in year between current zodiac and previous mentioned zodiac
    diff = zodiac_dict[zodiac] - zodiac_dict[cow_zodiac_map[mentioned_cow]]
    # expect diff to be negative since "previous"
    if diff >= 0:
      diff = diff - 12
    # add negative diff to the age of the mentioned cow
    cow_age_map[new_cow] = cow_age_map[mentioned_cow] + diff
  else:
    # get diff in year between current zodiac and previous mentioned zodiac
    diff =  zodiac_dict[zodiac] - zodiac_dict[cow_zodiac_map[mentioned_cow]]
    # expect diff to be positive since "next"
    if diff <= 0:
      diff += 12
    # add positive diff to the age of the mentioned cow
    cow_age_map[new_cow] = cow_age_map[mentioned_cow] + diff

print(abs(cow_age_map['Elsie']))