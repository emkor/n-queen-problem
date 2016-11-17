from constraint import SameDiagonalConstraint, SameColumnConstraint, SameRowConstraint
from csp import csp
from new_value_selectors import get_all_positions, get_free_positions, get_not_conflicted_positions
from utils import run_multiple_times, visualize_stats
import matplotlib.pyplot as plt

board_size = 8
constraints = [SameColumnConstraint(),
               SameRowConstraint(), SameDiagonalConstraint()]
get_all_positions_run_stats = run_multiple_times(times=3, function=csp,
                                                 params=[board_size, constraints, get_all_positions])
get_free_positions_run_stats = run_multiple_times(times=3, function=csp,
                                                  params=[board_size, constraints, get_free_positions])
get_not_conflicted_positions_run_stats = run_multiple_times(times=3, function=csp, params=[board_size, constraints,
                                                                                           get_not_conflicted_positions])
visualize_stats(get_all_positions_run_stats, "r", "get_all_positions_run_stats")
visualize_stats(get_free_positions_run_stats, "b", "get_free_positions_run_stats")
visualize_stats(get_not_conflicted_positions_run_stats, "g", "get_not_conflicted_positions_run_stats")
plt.show()
