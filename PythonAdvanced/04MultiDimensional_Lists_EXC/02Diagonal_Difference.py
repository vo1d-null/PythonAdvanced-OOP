n = (int(input()))

matrix = [[int(x) for x in input().split()] for _ in range(n)]

prime_sum = 0
sec_sum = 0

for i in range(n):
    prime_sum += matrix[i][i]
    sec_sum += matrix[i][n - i - 1]

print(abs(prime_sum-sec_sum))
