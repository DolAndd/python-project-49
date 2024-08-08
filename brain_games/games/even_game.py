from random import randint
EXERCISE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def get_question_and_right_answer():
    condition = randint(1, 100)
    right_answer = 'yes' if is_even(condition) else 'no'
    return str(condition), str(right_answer)
