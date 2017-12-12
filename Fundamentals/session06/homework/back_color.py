from random import *
from exercise_11 import is_inside

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():
    return [
                choice(shapes)['text'].upper(),
                choice(shapes)['color'],
                randint(0, 1)
            ]

def mouse_press(x, y, text, color, quiz_type):
    shape_info = {}

    if quiz_type == 0: # meaning
        for i in range(len(shapes)):
            if text == shapes[i]['text'].upper():
                shape_info = shapes[i]

    elif quiz_type == 1: # color
        for i in range(len(shapes)):
            if color == shapes[i]['color']:
                shape_info = shapes[i]

    check = is_inside([x, y], shape_info['rect'])
    if check:
        return True
    else:
        return False
