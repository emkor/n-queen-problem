class Constraint(object):
    def is_broken(self, chessboard):
        """
        :type chessboard: model.Chessboard
        :rtype: bool
        """
        raise NotImplementedError()


class SameColumnConstraint(Constraint):
    def is_broken(self, chessboard):
        x_positions = map(lambda queen: queen.x, chessboard.queens)
        return len(set(x_positions)) != len(x_positions)


class SameRowConstraint(Constraint):
    def is_broken(self, chessboard):
        y_positions = map(lambda queen: queen.y, chessboard.queens)
        return len(set(y_positions)) != len(y_positions)


class SameDiagonalConstraint(Constraint):
    def is_broken(self, chessboard):
        if chessboard.queen_count() > 1:
            for queen in chessboard.queens:
                for second_queen in (chessboard.queens[1:]):
                    if abs(second_queen.x - queen.x) == abs(second_queen.y - queen.y):
                        return True
                    else:
                        continue
        return False
