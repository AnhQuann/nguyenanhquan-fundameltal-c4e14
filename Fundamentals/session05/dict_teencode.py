teencode = {
    'vl': "Vui lắm",
    'hk': "Không"
}

while True:
    for key in teencode.keys():
        print(key, end=' ')
    print()

    word = input('Your code(Press Q to quit): ').lower()

    if word == 'q':
        break
    else:
        if word in teencode.keys():
            print(teencode[word])
            print('*' * 10)
        else:
            yes_no = input('Not found. Do you want add this code?(Y/N) ')
            if yes_no == 'Y' or yes_no == 'y':
                new_value = input('This code mean: ')
                teencode[word] = new_value
                print('*' * 10)
            else:
                print('*' * 10)

# sorted dictionary
