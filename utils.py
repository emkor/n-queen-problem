from datetime import datetime
import matplotlib.pyplot as plt


def visualize_stats(multiple_run_stats, color, label):
    """
    :type multiple_run_stats: list[list[model.Stat]]
    :type color: str
    :type label: str
    """
    plt.xlabel("Time (seconds)")
    plt.ylabel("properly placed queens")
    for run_stats in multiple_run_stats:
        iterations, seconds, values = split_to_iters_time_and_values(run_stats)
        plt.plot(seconds, values, "{}--".format(color), label=label)


def get_avg_iterations(mutliple_run_iterations):
    """
    :type mutliple_run_iterations: list[list[model.Stat]]
    :rtype: float
    """
    iterations_sum = 0
    for run_iterations in mutliple_run_iterations:
        iterations_sum += len(run_iterations)
    return float(iterations_sum) / float(len(mutliple_run_iterations))

def get_avg_seconds(mutliple_run_stats):
    """
    :type mutliple_run_iterations: list[list[model.Stat]]
    :rtype: float
    """
    time_sum = 0
    for run_stats in mutliple_run_stats:
        time_sum += max([stat.seconds for stat in run_stats])
    return float(time_sum) / float(len(mutliple_run_stats))

def split_to_iters_time_and_values(run_stats):
    """
    :type run_stats: list[model.Stat]
    :rtype tuple[list]
    """
    return zip(*[(stat.iteration, stat.seconds, stat.value) for stat in run_stats])


class DuplicateQueen(Exception):
    pass


class QueenOutOfChessboard(Exception):
    pass


class ChessboardIsEmpty(Exception):
    pass


def log(message):
    print("{} | {}".format(datetime.now(), message))


def run_multiple_times(times, function, params):
    multiple_run_stats = []
    for i in range(0, times):
        _, stats = function(*params)
        multiple_run_stats.append(stats)
    return multiple_run_stats


def display_chessboard(queens, chessboard_size):
    """
    :type queens: list[model.Queen]
    :type chessboard_size: int
    """
    print("".join(["-"] * ((chessboard_size * 3) + 2)))
    for y in range(0, chessboard_size):
        row = []
        for x in range(0, chessboard_size):
            queens_on_pos = filter(lambda queen: queen.x == x and queen.y == y, queens)
            row.append(" - " if not queens_on_pos else " X ")
        print(" {}|{}".format(y, "".join(row)) if y <= 9 else "{}|{}".format(y, "".join(row)))
    print("".join(["-"] * ((chessboard_size * 3) + 2)))


def seconds_since(start_time):
    """
    :type start_time: datetime
    :rtype: float
    """
    return (datetime.now() - start_time).total_seconds()


def are_queens_on_diagonal(first_queen, second_queen):
    """
    :type first_queen: model.Queen
    :type second_queen: model.Queen
    :return: bool
    """
    return abs(second_queen.x - first_queen.x) == abs(second_queen.y - first_queen.y)
