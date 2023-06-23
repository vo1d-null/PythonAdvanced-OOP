n = int(input())
flat = []
for _ in range(n):
    inner = [int(el) for el in input().split(', ')]
    flat.extend(inner)

print(flat)
