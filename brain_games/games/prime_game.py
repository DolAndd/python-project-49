from random import randint
EXERCISE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


def get_question_and_right_answer():
    condition = randint(2, 100)
    right_answer = 'yes' if is_prime(condition) else 'no'
    return str(condition), str(right_answer)
