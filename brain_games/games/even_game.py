from random import randint
exercise = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_conditions():
    random_number = randint(1, 100)
    condition = str(random_number)
    right_answer = ''
    if random_number % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return condition, right_answer
