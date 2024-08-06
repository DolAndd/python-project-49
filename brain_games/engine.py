from brain_games.cli import welcome_user
ATTEMPTS_NUMBER = 3


def play_games(game):
    player_name = welcome_user()
    print(game.EXERCISE)
    for i in range(ATTEMPTS_NUMBER):
        condition, right_answer = game.get_question_and_right_answer()
        print(f'Question: {condition}')
        answer = input('Your answer: ')
        if right_answer == answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. \
Correct answer was '{right_answer}'.")
            print(f"Let's try again, {player_name}!")
            return
    print(f'Congratulations, {player_name}!')
