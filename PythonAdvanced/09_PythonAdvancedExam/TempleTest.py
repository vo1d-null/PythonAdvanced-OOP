def solve_temple_challenges(tools_list, substances_list, challenges_list):
    """
    Given lists of tools, substances, and challenges, attempt to solve the challenges using the tools and substances.
    If successful, print the remaining tools and substances, along with a message indicating success.
    If unsuccessful, print a message indicating failure.
    """
    while tools_list and substances_list and challenges_list:
        tool = tools_list[0]
        substance = substances_list[-1]
        result = tool * substance
        if result in challenges_list:
            challenges_list.remove(result)
            if tools_list:
                tools_list.append(tools_list.pop(0) + 1)

            substances_list.pop()
    tools_list.append(tools_list.pop(0) + 1)
    substances_list[-1] -= 1
    if substances_list[-1] == 0:
        substances_list.pop()


    if not substances_list:
        print("Harry is lost in the temple. Oblivion awaits him.")
    else:
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
    if tools_list:
        print(f"Tools: {', '.join(str(t) for t in tools_list)}")
    if substances_list:
        print(f"Substances: {', '.join(str(s) for s in substances_list)}")
    if challenges_list:
        print(f"Challenges: {', '.join(str(c) for c in challenges_list)}")
try:
    tools = list(map(int, input("Enter tools: ").split()))
    substances = list(map(int, input("Enter substances: ").split()))
    challenges = list(map(int, input("Enter challenges: ").split()))
except ValueError:
    print("Invalid input. Please enter integers separated by spaces.")
else:
    solve_temple_challenges(tools, substances, challenges)
