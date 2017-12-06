from random import choice

word = 'champion'
characters1 = list(word)
characters2 = [None]*8

while len(characters1) > 0:
    for i in range(len(characters2)):
        characters2[i] = choice(characters1)
        characters1.remove(characters2[i])

for i, item in enumerate(characters2):
    print(item,' ', end='')
print()

while True:
    answer = input('Your answer: ')
    if answer != word:
        print('Wrong :(. Try again :D')
    else:
        print('Congratulation!')
        break
