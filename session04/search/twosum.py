numbers = [-79, -33, -5, 5, 33, 89, 130, 156]

found = False

for i in range(len(numbers)-1):
    for j in range(i + 1, len(numbers)-1):
        if numbers[i] + numbers[j] == 0:
            print(numbers[i],'+', numbers[j],'= 0')
            found = True

if not found:
    print('Not found')
