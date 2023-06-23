odd_set = set()
even_set = set()
for row in range(1, int(input()) + 1):
    ascii_sum_name = sum(ord(i) for i in input()) // row

    #Ternal opertor :        izpulni lqvo if true <- Uslovie -> izpulni dqsno if else
    even_set.add(ascii_sum_name) if ascii_sum_name % 2 == 0 else odd_set.add(ascii_sum_name)

if sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=', ')
else:
    print(*odd_set.symmetric_difference(even_set), sep=', ')
