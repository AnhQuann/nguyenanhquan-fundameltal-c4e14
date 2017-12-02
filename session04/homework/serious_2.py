numbers = [1, 6, 8, 1, 2, 1, 5, 6]

found = False

count = 0
x = int(input("What do you want to find?: "))
if x in numbers:
    found = True
    for i in range(len(numbers)):
        if numbers[i] == x:
            count+=1

if not found:
    print('Not found.')
else:
    print('{0} appears {1} times in my list.'.format(x, count))
