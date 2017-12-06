crud = ['C', 'R', 'U', 'D', 'c', 'r', 'u', 'd']
item = ['T-Shirt', 'Sweater']

while True:

    action = input('Welcome to our shop, what do you want (C, R, U, D)? ')

    if action not in crud:
        print("Please don't joke me! ")
    else:
        if action == 'C' or action == 'c':
            item_name = input('Enter new item: ')
            item.append(item_name)
            print('Our items: ', end='')
            print(*item, sep = ', ')
        elif action == 'R' or action == 'r':
            print('Our items: ', end='')
            print(*item, sep = ', ')
        elif action == 'U' or action == 'u':
            while True:
                print('Our items: ', end='')
                print(*item, sep = ', ')
                position = int(input('Update position? '))
                if position < 1 or position > len(item):
                    print('Just have 2 product and sort from number 1. Please try again!')
                else:
                    update_name = input('New item? ')
                    item[position-1] = update_name
                    print('Our items: ', end='')
                    print(*item, sep = ', ')
                    break
        elif action == 'D' or action == 'd':
            while True:
                print('Our items: ', end='')
                print(*item, sep = ', ')
                position = int(input('Delete position? '))
                if position < 1 or position > len(item):
                    print('Just have 2 product and sort from number 1. Please try again!')
                else:
                    del item[position-1]
                    print('Our items: ', end='')
                    print(*item, sep = ', ')
                    break

        break
