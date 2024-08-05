#!/usr/bin/env python3

from brain_games.games import progression_game
from brain_games.engine import play_games


def main():
    play_games(progression_game)


if __name__ == '__main__':
    main()
