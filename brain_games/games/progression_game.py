from random import randint
exercise = 'What number is missing in the progression?'
lenght_progression = 10


def game_conditions():
    start_progression = randint(1, 50)
    step_progression = randint(2, 5)
    pass_num_index = randint(0, lenght_progression - 1)
    progression = [str(start_progression + i * step_progression)
                   for i in range(lenght_progression)]
    right_answer = int(progression[pass_num_index])
    progression[pass_num_index] = '..'
    condition = ' '.join(progression)

    return condition, right_answer
