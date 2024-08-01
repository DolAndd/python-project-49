from random import randint
exercise = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_conditions():
    random_number = randint(2, 100)
    condition = str(random_number)
    right_answer = 0
    for i in range(2, random_number // 2 + 1):
        if random_number % i == 0:
            right_answer = 'no'
            break
    else:
        right_answer = 'yes'
    return condition, right_answer
