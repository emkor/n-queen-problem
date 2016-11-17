from constraint import SameDiagonalConstraint, SameColumnConstraint, SameRowConstraint
from model import Chessboard, any_constraint_broken, get_possible_values
from utils import log


def csp(N, constraints, n_queens=8, iteration_limit=10000):
    """
    :type N: int
    :type constraints: list[constraint.Constraint]
    :type n_queens: int
    :type iteration_limit: int
    :rtype: list[model.Queen]
    """

    def go(existing_queens, iteration=0):
        """
        :type existing_queens: list[model.Queen]
        :type iteration: int
        :rtype: list[model.Queen]
        """
        log("Iteration {}: current queen count: {} with config: {}".format(iteration, len(existing_queens),
                                                                           existing_queens))
        if any_constraint_broken(existing_queens, constraints):
            log("\tconstraints broken!")
            return None
        if len(existing_queens) >= n_queens:
            log("Found solution! Returning chessboard: {}".format(len(existing_queens)))
            return existing_queens
        if iteration > iteration_limit:
            log("Could not find solution.")
            return None
        possible_values = get_possible_values(existing_queens, N)
        if not possible_values:
            return None
        else:
            log("\tstill has {} possible queens: {}".format(len(possible_values), possible_values))
            return next((go(existing_queens + [possible_value], iteration + 1) for possible_value in possible_values),
                        None)

    return go(existing_queens=[])


board_size = 5
queen_count = 4
constraints = [SameColumnConstraint(),
               SameRowConstraint(), SameDiagonalConstraint()]
var = csp(board_size, constraints, n_queens=queen_count)
print()
