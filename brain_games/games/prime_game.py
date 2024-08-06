from random import randint
EXERCISE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return 'no'
    return 'yes'


def get_question_and_right_answer():
    random_number = randint(2, 100)
    condition = str(random_number)
    right_answer = is_prime(random_number)
    return condition, str(right_answer)
