from random import randint
EXERCISE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return 'yes' if num % 2 == 0 else 'no'


def get_question_and_right_answer():
    random_number = randint(1, 100)
    condition = str(random_number)
    right_answer = is_even(random_number)
    return condition, str(right_answer)
