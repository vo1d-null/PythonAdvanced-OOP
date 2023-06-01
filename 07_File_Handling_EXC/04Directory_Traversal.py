import  os

def save_extensions(dir_name,first_level=False):
    for filename in os.listdir(dir_name):
        file = os.path.join(dir_name, filename)

        if os.path.isfile(file):
            extension = filename.split('.')[-1]
            if extension not in extensions:
                extensions[extension] = []

            extensions[extension].append(filename)
        elif os.path.isdir(file) and not first_level:
            save_extensions(file, first_level=True)


directory = input()

extensions = {

}
report = []

try:
    save_extensions(directory)
except FileNotFoundError:
    print('Directory is not valid!')

extensions = sorted(extensions.items(), key=lambda x: x[0])

for extension, files in extensions:
    report.append(f'{extension}')

    [report.append(f'- - - {file}') for file in sorted(files)]

with open('files/report.txt', 'w') as file:
    file.write('\n'.join(report))
