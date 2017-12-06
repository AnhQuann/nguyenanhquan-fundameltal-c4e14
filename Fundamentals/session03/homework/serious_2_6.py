ship_size = [5, 7, 300, 90, 24, 50, 75]

print('Hello, my name is Hiep and these are my ship sizes')
print(ship_size)
print()

for month in range(3):
    print('MONTH', month+1, ":")

    for j in range(len(ship_size)):
        if ship_size[j] == max(ship_size):
            ship_size[j] = 8
            break
    print('One month has passed, now here is my flock')
    print(ship_size)
    print('Now my biggest sheep has size', max(ship_size), "let's shear it")

    for i in range(len(ship_size)):
        ship_size[i] = ship_size[i] + 50
    print('After shearing, here is my flock')
    print(ship_size)
    print()

total_size = 0

for i in range(len(ship_size)):
    total_size += ship_size[i]
    
print('My flock has size in total:', total_size)
print('I would get', total_size, '* 2$ =', total_size*2)
