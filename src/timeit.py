import sys
import time


def timeit(method):
    """
    Decorator: Compute the execution time of a function
    :param method: the function
    :return: the method runtime
    """

    def timed(*arguments, **kw):
        ts = time.time()
        result = method(*arguments, **kw)
        te = time.time()

        print('Time:  %r %2.2f sec\n' % (method.__name__.strip("_"), te - ts))
        print('------------------------------------\n')
        return result

    return timed
