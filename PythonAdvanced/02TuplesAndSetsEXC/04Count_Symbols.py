# occs = {}
# for letter in input():
#    occs[letter] = occs.get(letter, 0) + 1
#
# for letter, times in sorted(occs.items()):
#   print(f"{letter}: {times} time/s")

text = input()
for letter in sorted(set(text)):
    print(f"{letter}: {text.count(letter)} time/s")
