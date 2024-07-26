from random import randint
from brain_games.cli import welcome_user


def guess_even_number():
    player_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    true_answer_count = 0
    for i in range(3):
        random_number = randint(1, 100)
        print('Question:', random_number)
        print('Your answer: ', end ='')
        answer = input()
        right_answer = ''
        if random_number % 2 == 0:
            right_answer = 'yes'
        else:
            right_answer = 'no'
        if right_answer == answer:
            print('Correct!')
            true_answer_count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. \
Correct answer was '{right_answer}'.")
            print("Let's try again, Bill!")
            break
    else:
        print('Congratulations, Bill!')
