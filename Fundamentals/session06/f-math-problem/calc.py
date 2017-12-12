from random import randint
from random import choice
# def add(x, y): # no argument
#     print(x + y)
def evaluate(x, y, operator):
    result = 0
    if(operator == '+'):
        result = x+y
    elif(operator == '-'):
        result = x-y
    elif(operator == '*'):
        result = x*y
    elif(operator == '/'):
        result = x/y
    return result

# x = randint(0,10)
# y = randint(0,10)
# operator = choice(['+', '-', '*', '/'])
# z = evaluate(x, y, operator)
# print('{0}{1}{2} = {3}'.format(x, operator, y, z))

print(__name__ )
