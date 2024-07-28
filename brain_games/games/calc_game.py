from random import randint, choice
exercise = 'What is the result of the expression?'


def game_conditions():
    num1 = randint(1, 20)
    num2 = randint(1, 20)
    operation = choice('+-*')
    condition = f'{num1} {operation} {num2}'
    right_answer = 0
    if operation == '+':
        right_answer = num1 + num2
    elif operation == '-':
        right_answer = num1 - num2
    else :
        right_answer = num1 * num2
    return condition, right_answer
