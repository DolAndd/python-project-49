from brain_games.cli import welcome_user
attempts_number = 3


def play_games(game):
    player_name = welcome_user()
    true_answer_count = 0
    print(game.exercise)
    for i in range(attempts_number):
        condition, right_answer = game.game_conditions()
        print(f'Question: {condition}')
        print('Your answer: ', end='')
        answer = input()
        if str(right_answer) == answer:
            print('Correct!')
            true_answer_count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. \
Correct answer was '{right_answer}'.")
            print(f"Let's try again, {player_name}")
            break
    else:
        print(f'Congratulations, {player_name}')
