from utils import are_queens_on_diagonal


class Constraint(object):
    def is_broken(self, queens):
        """
        :type queens: list[model.Queen]
        :rtype: bool
        """
        raise NotImplementedError()


class SameColumnConstraint(Constraint):
    def is_broken(self, queens):
        x_positions = map(lambda queen: queen.x, queens)
        return len(set(x_positions)) != len(x_positions)


class SameRowConstraint(Constraint):
    def is_broken(self, queens):
        y_positions = map(lambda queen: queen.y, queens)
        return len(set(y_positions)) != len(y_positions)


class SameDiagonalConstraint(Constraint):
    def is_broken(self, queens):
        if len(queens) > 1:
            for index, queen in enumerate(queens[:-1]):
                for second_queen in queens[index + 1:]:
                    if are_queens_on_diagonal(queen, second_queen):
                        return True
                    else:
                        continue
        return False


