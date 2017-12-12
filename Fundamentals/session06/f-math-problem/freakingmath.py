from random import *
from calc import evaluate
from random import randint



def generate_quiz():
    x = randint(0,10)
    y = randint(1,10)
    op = choice(['+', '-', '*', '/'])
    result = evaluate(x, y, op)+randint(-2,2)
    # Hint: Return [x, y, op, result]
    return [x, y, op, result]

def check_answer(x, y, op, result, user_choice):
    real_result = evaluate(x, y, op)
    if user_choice:
        return real_result = result
    else:
        return not real_result = result
