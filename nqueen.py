from collections import Counter
from random import randint

from datetime import datetime


class DuplicateQueen(Exception):
    pass


class QueenOutOfChessboard(Exception):
    pass


class ChessboardIsEmpty(Exception):
    pass


class Queen(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(tuple([self.x, self.y]))

    def __str__(self):
        return "Queen <{}, {}>".format(self.x, self.y)

    def __repr__(self):
        return self.__str__()


def get_random_queen(n):
    x = randint(0, n - 1)
    y = randint(0, n - 1)
    return Queen(x, y)


class Chessboard(object):
    def __init__(self, n):
        self.n = n
        self.queens = []

    def count_conflicts(self):
        same_position_conflicts = len(self.queens) - len(set(self.queens))
        same_x_conflicts = sum(filter(lambda occurences: occurences > 1,
                                      Counter(map(lambda queen: queen.x, self.queens)).values()))
        same_y_conflicts = sum(filter(lambda occurences: occurences > 1,
                                      Counter(map(lambda queen: queen.y, self.queens)).values()))
        diagonal_conflicts = 0
        if self.queen_count() > 1:
            for queen in self.queens:
                for second_queen in (self.queens[1:]):
                    if abs(second_queen.x - queen.x) == abs(second_queen.y - queen.y):
                        diagonal_conflicts += 1
        return same_x_conflicts + same_y_conflicts + same_position_conflicts + diagonal_conflicts

    def add_queen(self, queen):
        if self.n > queen.x >= 0 and self.n > queen.y >= 0:
            if queen not in self.queens:
                self.queens.append(queen)
            else:
                raise DuplicateQueen("{} is already on chessboard".format(queen))
        else:
            raise QueenOutOfChessboard("{} is out of chessboard".format(queen))

    def remove_last_queen(self):
        if self.queen_count() > 0:
            return self.queens.pop()
        else:
            raise ChessboardIsEmpty("Could not remove queen from empty chessboard")

    def free_xs_list(self):
        initial = range(0, self.n - 1)
        for queen in self.queens:
            initial.remove(queen.x)
        return initial

    def free_ys_list(self):
        initial = range(0, self.n - 1)
        for queen in self.queens:
            initial.remove(queen.y)
        return initial

    def queen_count(self):
        return len(self.queens)


def log(message):
    print("{} | {}".format(datetime.now(), message))


def csp(chessboard, iter_limit, queen_n):
    """
    :type chessboard: nqueen.Chessboard
    :type iter_limit: int
    :type queen_n: int
    :rtype: nqueen.Chessboard
    """
    if chessboard.count_conflicts() <= 0:
        if chessboard.queen_count() >= queen_n:
            log("Found solution! Returning chessboard...")
            return chessboard
        new_queen = _keep_iterating_until_not_duplicated(chessboard, iter_limit)
        try:
            log("Adding new {} ...".format(new_queen))
            chessboard.add_queen(new_queen)
            return csp(chessboard, iter_limit, queen_n)
        except DuplicateQueen as e:
            log(e)
            return chessboard
    else:
        removed_queen = chessboard.remove_last_queen()
        log("Could not add {} due to conflicts".format(removed_queen))
        return csp(chessboard, iter_limit, queen_n)


def _keep_iterating_until_not_duplicated(chessboard, iter_limit):
    new_queen = get_random_queen(chessboard.n)
    iteration = 0
    while iteration <= iter_limit and new_queen in chessboard.queens:
        new_queen = get_random_queen(chessboard.n)
        iteration += 1
    return new_queen


chessboard_size = 8
queen_count = 4
iterations_limit = 100
csp(Chessboard(chessboard_size), iterations_limit, queen_count)
