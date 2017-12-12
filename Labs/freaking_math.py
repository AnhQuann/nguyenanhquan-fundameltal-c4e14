from random import randint
from random import choice
x = randint(0,10)
y = randint(0,10)

operator = ['+', '-', '*', '/']
calc = choice(operator)

if calc == '+':
    real_result = x+y
    false_result = real_result + randint(-2, 2)
elif calc == '-':
    real_result = x-y
    false_result = real_result + randint(-2, 2)
elif calc == '*':
    real_result = x*y
    false_result = real_result + randint(-2, 2)
elif calc == '/':
    real_result = x/y
    false_result = real_result + randint(-2, 2)

print('{0} {1} {2} = '.format(x, calc, y), false_result)

score = 0
answer = input('Y/N?')
if answer == 'Y':
    if real_result == false_result:
        print('Đúng')
        score += 1
        print('Now Your score is {0}'.format(score))
    else:
        print('Sai')
        break

if answer == 'N':
    if real_result != false_result:
        print('Đúng')
        score += 1
        print('Now Your score is {0}'.format(score))
    else:
        print('Sai')
        break
