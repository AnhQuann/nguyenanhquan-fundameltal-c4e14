menu = ['com', 'kem', 'keo']

for i, item in enumerate(menu):
    print(i + 1, item, sep = ". ")
position = int(input('Position u want to upate:'))
content = input('Replace: ')

menu[position-1] = content
for i, item in enumerate(menu):
    print(i + 1, item, sep = ". ")

# for i, item in enumerate(menu):
#     print(i + 1, item, sep = ". ")
