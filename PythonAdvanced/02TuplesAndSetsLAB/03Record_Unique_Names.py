n = int(input())
names_set = set({})
for _ in range(n):
    names_set.add(input())
for names in names_set:
    print(names)
