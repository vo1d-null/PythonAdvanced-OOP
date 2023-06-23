n, m = input().split()
n, m = int(n), int(m)

a, b = set(), set()

for _ in range(n):
    a.add(input())

for _ in range(m):
    b.add(input())

print(*a.intersection(b), sep='\n')

