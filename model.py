from utils import DuplicateQueen, QueenOutOfChessboard, ChessboardIsEmpty


def any_constraint_broken(queens, constraints):
    """
    :type queens: list[model.Queen]
    :type constraints: list[constraint.Constraint]
    :rtype: bool
    """
    return any(map(lambda constraint: constraint.is_broken(queens), constraints))


class Stat(object):
    def __init__(self, iteration, seconds, value):
        """
        :type iteration: int
        :type seconds: float
        :type value: int
        """
        self.iteration = iteration
        self.seconds = seconds
        self.value = value

    def __str__(self):
        return "Stat<#{} was {}, {}s>".format(self.iteration, self.value, self.seconds)

    def __repr__(self):
        return self.__str__()


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
