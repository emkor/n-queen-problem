from random import randint

from utils import DuplicateQueen, QueenOutOfChessboard, ChessboardIsEmpty


def any_constraint_broken(queens, constraints):
    """
    :type queens: list[model.Queen]
    :type constraints: list[constraint.Constraint]
    :rtype: bool
    """
    return any(map(lambda constraint: constraint.is_broken(queens), constraints))


def get_possible_values(queens, n):
    """
    :type queens: list[model.Queen]
    :type n: int
    :rtype: set[model.Queen]
    """
    possible_queens = set()
    for x in range(0, n):
        for y in range(0, n):
            possible_queens.add(Queen(x, y))
    return set(possible_queens - set(queens))


def get_random_queen(n):
    """
    :type n: int
    :rtype: model.Queen
    """
    x = randint(0, n - 1)
    y = randint(0, n - 1)
    return Queen(x, y)


class Queen(object):
    def __init__(self, x, y):
        """
        :type x: int
        :type y: int
        """
        self.x = x
        self.y = y

    def __eq__(self, other):
        """
        :type other: model.Queen
        """
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(tuple([self.x, self.y]))

    def __str__(self):
        return "Queen <{}, {}>".format(self.x, self.y)

    def __repr__(self):
        return self.__str__()


class Chessboard(object):
    def __init__(self, n):
        """
        :type n: int
        """
        self.n = n
        self.queens = []

    def add_queen(self, queen):
        """
        :type queen: model.Queen
        :rtype queen: model.Chessboard
        """
        if self.n > queen.x >= 0 and self.n > queen.y >= 0:
            if queen not in self.queens:
                self.queens.append(queen)
                return self
            else:
                raise DuplicateQueen("{} is already on chessboard".format(queen))
        else:
            raise QueenOutOfChessboard("{} is out of chessboard".format(queen))

    def remove_last_queen(self):
        if self.queen_count() > 0:
            return self.queens.pop()
        else:
            raise ChessboardIsEmpty("Could not remove queen from empty chessboard")

    def queen_count(self):
        return len(self.queens)

    def __str__(self):
        return "Chessboard with {} queens: <{}>".format(self.queen_count(),
                                                        ", ".join(map(lambda queen: str(queen), self.queens)))

    def __repr__(self):
        return self.__str__()
