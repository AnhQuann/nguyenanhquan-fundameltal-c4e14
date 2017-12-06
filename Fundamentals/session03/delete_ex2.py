menu = ['com', 'kem', 'keo']

for i, item in enumerate(menu):
    print(i + 1, item, sep = ". ")

while True:
    content = input('What do want to delete: ')
    if content not in menu:
        print("Loi")
    else:
        menu.remove(content)

        for i, item in enumerate(menu):
            print(i + 1, item, sep = ". ")
        break
