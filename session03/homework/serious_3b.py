from random import choice

word = ['yasuo', 'leesin', 'teemo']
main_word = choice(word)
characters1 = list(main_word)
characters2 = [None]*len(characters1)

while len(characters1) > 0:
    for i in range(len(characters2)):
        characters2[i] = choice(characters1)
        characters1.remove(characters2[i])

for i, item in enumerate(characters2):
    print(item,' ', end='')
print()

while True:
    answer = input('Your answer: ')
    if answer != main_word:
        print('Wrong :(. Try again :D')
    else:
        print('Congratulation!')
        break
