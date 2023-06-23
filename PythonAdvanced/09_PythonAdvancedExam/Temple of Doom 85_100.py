from collections import deque

tools = deque([int(i) for i in input().split()])
substances = deque([int(i) for i in input().split()])
challenges = deque([int(i) for i in input().split()])

while tools and substances:
    tool = tools.popleft()
    substance = substances.pop()
    result = tool * substance

    if len(challenges) <= 0:
        break

    if result in challenges:
        challenges.remove(result)
        continue

    tool += 1
    tools.append(tool)
    substance -= 1
    if substance <= 0:
        continue
    else:
        substances.append(substance)

if len(challenges) > 0:
    print('Harry is lost in the temple. Oblivion awaits him.')

if len(challenges) == 0:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

if tools:
    print('Tools: ', end='')
    print(*tools, sep=', ')

if substances:
    print('Substances: ', end='')
    print(*substances, sep=', ')

if challenges:
    print('Challenges: ', end='')
    print(*challenges, sep=', ')