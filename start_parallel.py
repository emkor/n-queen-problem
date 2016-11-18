from multiprocessing import Process


def run_in_parallel(function_to_params):
    """
    :type function_to_params: dict
    """
    proc = []
    for fn, params in function_to_params.iteritems():
        p = Process(target=fn, args=params)
        p.start()
        proc.append(p)
    for p in proc:
        p.join()
