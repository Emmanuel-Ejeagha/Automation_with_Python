from pathlib import Path

p1 = Path('files/w.txt')
# print(type(p1))

# if p1.exists():
#     with open(p1, 'r') as file:
#         print(file.read())


if not p1.exists():
    with open(p1, 'w') as file:
        file.write('Content 3')