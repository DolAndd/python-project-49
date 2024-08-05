from brain_games.cli import welcome_user
attempts_number = 3


def play_games(game):
    player_name = welcome_user()
    true_answer_count = 0
    print(game.EXERCISE)
    for i in range(attempts_number):
        condition, right_answer = game.get_question_and_right_answer()
        print(f'Question: {condition}')
        answer = input('Your answer: ')
        if right_answer == answer:
            print('Correct!')
            true_answer_count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. \
Correct answer was '{right_answer}'.")
            print(f"Let's try again, {player_name}!")
            return
    print(f'Congratulations, {player_name}!')
