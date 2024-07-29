from random import randint
exercise = 'Find the greatest common divisor of given numbers.'


def game_conditions():
    num1 = randint(1, 30)
    num2 = randint(1, 30)
    condition = f'{num1} {num2}'
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    right_answer = num1 + num2
    return condition, right_answer
