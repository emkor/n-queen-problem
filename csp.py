from datetime import datetime
from model import any_constraint_broken
from stats import Stat
from utils import log, seconds_since


def csp(N, constraints, new_value_selector_function, timeout=10):
    """
    :type N: int
    :type constraints: list[constraint.Constraint]
    :type timeout: int
    :rtype: list[model.Queen]
    """

    def go(existing_queens):
        """
        :type existing_queens: list[model.Queen]
        :rtype: list[model.Queen]
        """
        if seconds_since(start_time) > timeout:
            log("TIMEOUT! Could not find solution in {} seconds.".format(timeout))
            return None
        # log("Current queen count: {} with config: {}".format(len(existing_queens), existing_queens))
        if any_constraint_broken(existing_queens, constraints):
            return None
        stats.append(Stat(len(stats), seconds_since(start_time), len(existing_queens)))
        if len(existing_queens) >= N:
            log("Found solution! Returning chessboard: {}".format(existing_queens))
            return existing_queens
        possible_values = new_value_selector_function(existing_queens, N)
        if N - len(existing_queens) > len(possible_values):
            # log("\tforwardcheck, need {} more values, but possible is only {}".format(N - len(existing_queens),
            #                                                                           len(possible_values)))
            return None
        else:
            # log("\twith: {} existing: {} possible: {}".format(new_value_selector_function.func_name,
            #                                                   len(existing_queens), len(possible_values)))
            for possible_queen in possible_values:
                queens = go(existing_queens + [possible_queen])
                if queens is not None:
                    return queens
            return None

    stats = []
    start_time = datetime.now()
    log("Initializing with {} as new value generator".format(new_value_selector_function.func_name))
    return go(existing_queens=[]), stats
