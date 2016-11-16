from random import randint

from utils import DuplicateQueen, QueenOutOfChessboard, ChessboardIsEmpty


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

    # def count_conflicts(self):
    #     same_position_conflicts = len(self.queens) - len(set(self.queens))
    #     same_x_conflicts = sum(filter(lambda occurences: occurences > 1,
    #                                   Counter(map(lambda queen: queen.x, self.queens)).values()))
    #     same_y_conflicts = sum(filter(lambda occurences: occurences > 1,
    #                                   Counter(map(lambda queen: queen.y, self.queens)).values()))
    #     diagonal_conflicts = 0
    #     if self.queen_count() > 1:
    #         for queen in self.queens:
    #             for second_queen in (self.queens[1:]):
    #                 if abs(second_queen.x - queen.x) == abs(second_queen.y - queen.y):
    #                     diagonal_conflicts += 1
    #     return same_x_conflicts + same_y_conflicts + same_position_conflicts + diagonal_conflicts

    def add_queen(self, queen):
        """
        :type queen: model.Queen
        """
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

    def queen_count(self):
        return len(self.queens)
