n = (int(input()))

matrix = [[int(x) for x in input().split(', ')] for _ in range(n)]
prime_dia = [matrix[r][r] for r in range(n)]
sec_dia = [matrix[r][n - r -1] for r in range(n)]

print(f"Primary diagonal: {', '.join(str(x) for x in prime_dia)}. Sum: {sum(prime_dia)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in sec_dia)}. Sum: {sum(sec_dia)}")
