first_seq = set(int(x) for x in input().split())
second_seq = set(int(x) for x in input().split())

functions = {
    "Add First": lambda x: [first_seq.add(el) for el in x],
    "Add Second": lambda x: [second_seq.add(el) for el in x],
    "Remove First": lambda x: [first_seq.discard(el) for el in x],
    "Remove Second": lambda x: [second_seq.discard(el) for el in x],
    "Check Subset": lambda x: print(first_seq.issubset(second_seq) or second_seq.issubset(first_seq)),
}

for _ in range(int(input())):
    first_command, second_command, *data = input().split()
    command = first_command + " " + second_command

    functions[command](int(x) for x in data)
print(*sorted(first_seq), sep=", ")
print(*sorted(second_seq), sep=", ")
