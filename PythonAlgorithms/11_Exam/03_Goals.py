def find_best_sequence(goals):
    n = len(goals)
    dp = [1] * n
    prev = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if goals[i] >= goals[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j

    max_length = max(dp)
    idx = dp.index(max_length)

    sequence = []
    while idx != -1:
        sequence.insert(0, goals[idx])
        idx = prev[idx]

    return sequence


input_goals = input().split(', ')
goals = [int(goal) for goal in input_goals]
best_sequence = find_best_sequence(goals)
print(' '.join(map(str, best_sequence)))
