ship_size = [5, 7, 300, 90, 24, 50, 75]

print('Hello, my name is Hiep and these are my ship sizes')
print(ship_size)
print()

print('Now my biggest sheep has size', max(ship_size), "let's shear it")
print()

for i in range(len(ship_size)):
    if ship_size[i] == max(ship_size):
        ship_size[i] = 8
        break
print('After shearing, here is my flock')
print(ship_size)
print()

for i in range(len(ship_size)):
    ship_size[i] = ship_size[i] + 50
print('One month has passed, now here is my flock')
print(ship_size)
print()
