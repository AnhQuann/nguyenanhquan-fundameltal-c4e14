menu = ['com', 'kem', 'keo']

for i, item in enumerate(menu):
    print(i + 1, item, sep = ". ")

while True:
    position = int(input('Position u want to delete:'))

    if position<1 or position>len(menu):
        print("Loi")
    else:
        del menu[position-1]
        for i, item in enumerate(menu):
            print(i + 1, item, sep = ". ")
        break
