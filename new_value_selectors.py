from random import shuffle

import operator

from model import Queen
from utils import are_queens_on_diagonal, log


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
    all_positions = set(get_all_positions([], chessboard_size))
    possible_queens = list(all_positions - set(existing_queens))
    shuffle(possible_queens)
    return possible_queens


def get_not_conflicted_positions_sorted_by_efficiency(existing_queens, chessboard_size):
    """
    :type existing_queens: list[model.Queen]
    :type chessboard_size: int
    :rtype: list[model.Queen]
    """
    available_queens = get_not_conflicted_positions(existing_queens, chessboard_size)
    available_queen_to_taken_slots = _build_available_queen_to_efficiency_dict(existing_queens, available_queens,
                                                                               chessboard_size)
    available_queens_sorted_by_efficiency = sorted(available_queen_to_taken_slots.items(), key=operator.itemgetter(1))
    available_queens_sorted_by_efficiency.reverse()
    return [queen for queen, efficiency in available_queens_sorted_by_efficiency]


def _build_available_queen_to_efficiency_dict(existing_queens, available_queens, n):
    """
    :type existing_queens: list[model.Queen]
    :type available_queens: list[model.Queen]
    :type n: int
    :rtype: dict[model.Queen, int]
    """
    return {avail_queen: len(get_not_conflicted_positions(existing_queens + [avail_queen], n)) for avail_queen in
            available_queens}


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
