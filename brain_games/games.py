from random import randint
from brain_games.cli import welcome_user


def guess_even_number():
    player_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    true_answer_count = 0
    while true_answer_count < 3:
        random_number = randint(1, 100)
        print('Question:', random_number)
        print('Your answer: ', end='')
        answer = input()

        if (random_number % 2 == 0 and answer == 'yes') or \
           (random_number % 2 == 1 and answer == 'no'):
            print('Correct!')
            true_answer_count += 1
        elif random_number % 2 == 0 and answer != 'yes':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {player_name}")
            true_answer_count = 0
        elif random_number % 2 == 1 and answer != 'no':
            print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {player_name}")
            true_answer_count = 0
    print(f'Congratulations, {player_name}')
