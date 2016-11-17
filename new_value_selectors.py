from random import shuffle

from model import Queen
from utils import are_queens_on_diagonal


def get_all_positions(existing_queens, chessboard_size):
    """
    :type existing_queens: list[model.Queen]
    :type chessboard_size: int
    :rtype: set[model.Queen]
    """
    possible_queens = set()
    for x in range(0, chessboard_size):
        for y in range(0, chessboard_size):
            possible_queens.add(Queen(x, y))
    possible_queens = list(possible_queens)
    shuffle(possible_queens)
    return possible_queens


def get_free_positions(existing_queens, chessboard_size):
    """
    :type existing_queens: list[model.Queen]
    :type chessboard_size: int
    :rtype: list[model.Queen]
    """
    possible_queens = list(set(get_all_positions([], chessboard_size)) - set(existing_queens))
    shuffle(possible_queens)
    return possible_queens


def get_not_conflicted_positions(existing_queens, chessboard_size):
    """
    :type existing_queens: list[model.Queen]
    :type chessboard_size: int
    :rtype: list[model.Queen]
    """
    possible_queens = list(get_all_positions([], chessboard_size=chessboard_size))
    for existing in existing_queens:
        possible_queens = filter(
            lambda possible:
            possible.x != existing.x
            and possible.y != existing.y
            and not are_queens_on_diagonal(existing, possible),
            possible_queens)
    shuffle(possible_queens)
    return possible_queens
