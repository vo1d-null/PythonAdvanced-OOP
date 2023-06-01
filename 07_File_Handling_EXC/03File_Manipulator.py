while True:
    command, *info = input().split('-')

    if command == 'Create':
        with open(f'files/{info[0]}', 'w') as file:
            file.write(info[1])
    elif command == 'Add':
        pass
    elif command == 'Replace':
        pass
    elif command == 'Delete':
        pass
    elif command == 'End':
        break