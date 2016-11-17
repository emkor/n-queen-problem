from constraint import SameColumnConstraint, SameRowConstraint, SameDiagonalConstraint
from model import get_random_queen, Chessboard, Queen
from utils import log, DuplicateQueen, get_possible_values, any_constraint_broken


def csp(N, constraints, n_queens=8, iterations=10000):
    """
    :type N: int
    :type constraints: list[constraint.Constraint]
    :type n_queens: int
    :type iterations: int
    :rtype: model.Chessboard
    """

    def go(chessboard, iteration, possible_values):
        """
        :type chessboard: model.Chessboard
        :type iteration: int
        :type possible_values: set[model.Queen]
        :rtype: model.Chessboard
        """
        log("Iteration {}: current queen count: {}".format(iterations, chessboard.queen_count()))
        if chessboard.queen_count() >= n_queens:
            log("Found solution! Returning chessboard: {}".format(chessboard))
            return chessboard
        if iterations < 0:
            log("Could not find solution.")
            return None

        possible_values = get_possible_values(chessboard) if possible_values is None else possible_values
        if not possible_values:
            conflicting_queen = chessboard.remove_last_queen()
            return go(chessboard, iteration + 1, get_possible_values(chessboard) - set(conflicting_queen))

        log("\tstill has {} possible queens: {}".format(len(possible_values), possible_values))
        for possible_value in possible_values:
            chessboard.add_queen(possible_value)
            log("\tadded {}".format(possible_value))
            if any_constraint_broken(chessboard, constraints):
                conflicting_queen = chessboard.remove_last_queen()
                possible_values.remove(conflicting_queen)
                log("\rremoved {}".format(conflicting_queen))
            return go(chessboard, iteration + 1, possible_values)

    new_chessboard = Chessboard(N)
    return go(chessboard=new_chessboard, iteration=0, possible_values=get_possible_values(new_chessboard))


board_size = 5
queen_count = 4
constraints = [SameColumnConstraint(), SameRowConstraint(), SameDiagonalConstraint()]
# csp = Csp(chessboard=Chessboard(board_size), constraints=constraints, n_queens=queen_count)
# csp.run()
csp(board_size, constraints, n_queens=queen_count, iterations=10000)
