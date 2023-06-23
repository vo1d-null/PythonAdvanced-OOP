num = int(input())
table = set()
for _ in range(num):
    for el in input().split(" "):
        table.add(el)
print(*table, sep='\n')
