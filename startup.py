from constraint import SameDiagonalConstraint, SameColumnConstraint, SameRowConstraint
from csp import csp
from new_value_selectors import get_all_positions, get_free_positions, get_not_conflicted_positions, \
    get_not_conflicted_positions_sorted_by_efficiency
from utils import run_multiple_times, visualize_stats, log, get_avg_seconds
import matplotlib.pyplot as plt

BOARD_SIZE = 8
REPEAT = 10
CONSTRAINTS = [SameColumnConstraint(),
               SameRowConstraint(), SameDiagonalConstraint()]

get_all_positions_run_stats = run_multiple_times(times=REPEAT, function=csp,
                                                 params=[BOARD_SIZE, CONSTRAINTS, get_all_positions])
get_free_positions_run_stats = run_multiple_times(times=REPEAT, function=csp,
                                                  params=[BOARD_SIZE, CONSTRAINTS, get_free_positions])
get_not_conflicted_positions_run_stats = run_multiple_times(times=REPEAT, function=csp, params=[BOARD_SIZE, CONSTRAINTS,
                                                                                                get_not_conflicted_positions])

get_weighted_positions_run_stats = run_multiple_times(times=REPEAT, function=csp, params=[BOARD_SIZE, CONSTRAINTS,
                                                                                          get_not_conflicted_positions_sorted_by_efficiency])

all_positions_avg_iters = get_avg_seconds(get_all_positions_run_stats)
log("CSP with get_all_positions as value generator has avg time: {}".format(all_positions_avg_iters))

free_positions_avg_iters = get_avg_seconds(get_free_positions_run_stats)
log("CSP with get_free_positions_run_stats as value generator has avg time: {}".format(free_positions_avg_iters))

not_conflicted_positions_avg_iters = get_avg_seconds(get_not_conflicted_positions_run_stats)
log("CSP with get_not_conflicted_positions_run_stats as value generator has avg time: {}".format(
    not_conflicted_positions_avg_iters))

get_weighted_positions_run_stats_avg_iters = get_avg_seconds(get_weighted_positions_run_stats)
log("CSP with get_weighted_positions_run_stats as value generator has avg time: {}".format(
    get_weighted_positions_run_stats_avg_iters))

visualize_stats(get_all_positions_run_stats, "r", "get_all_positions_run_stats")
visualize_stats(get_free_positions_run_stats, "b", "get_free_positions_run_stats")
visualize_stats(get_not_conflicted_positions_run_stats, "g", "get_not_conflicted_positions_run_stats")
visualize_stats(get_weighted_positions_run_stats, "m", "get_not_conflicted_positions_run_stats")
plt.show()
