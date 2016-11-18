class RunStats(object):
    def __init__(self, n, found_board, used_generative_function, stats):
        """
        :type n: int
        :type found_board: list[model.Queen]
        :type stats: list[stats.Stat]
        """
        self.n = n
        self.used_generative_function = used_generative_function
        self.found_board = found_board
        self.stats = stats

    def run_time(self):
        """
        :rtype: float
        """
        return self.stats[-1].seconds

    def iterations(self):
        """
        :rtype: int
        """
        return self.stats[-1].iteration

    def is_successful(self):
        """
        :rtype: bool
        """
        return self.found_board is not None

    def __str__(self):
        return "Stats for {} run with n={} and {} used. Time: {} Iterations: {}".format(
            "successful" if self.is_successful() else "failed", self.n, self.used_generative_function.func_name,
            self.run_time(), self.iterations())

    def __repr__(self):
        return self.__str__()


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
