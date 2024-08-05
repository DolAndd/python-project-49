#!/usr/bin/env python3

from brain_games.games import gcd_game
from brain_games.engine import play_games


def main():
    play_games(gcd_game)


if __name__ == '__main__':
    main()
