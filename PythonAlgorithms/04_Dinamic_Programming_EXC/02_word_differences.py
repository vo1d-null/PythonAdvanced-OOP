first_str = input()
second_srt = input()

dp = []

rows = len(first_str) + 1
cols = len(second_srt) + 1

for _ in range(rows):
    dp.append([0] * cols)


for col in range(1, cols):
    dp[0][col] = col


for row in range(1, rows):
    dp[row][0] = row

for row in range(1, rows):
    for col in range(1, cols):

        if first_str[row - 1] == second_srt[col - 1]:

            dp[row][col] = dp[row - 1][col - 1]

        else:
            dp[row][col] = min(dp[row][col - 1], dp[row - 1][col]) + 1

print(f'Deletions and Insertions: {dp[rows - 1][cols - 1]}')