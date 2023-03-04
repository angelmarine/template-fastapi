# -*- coding: utf-8 -*-

import sys
import time
from functools import wraps


def get_console_logger():
    """Returns a multiprocess-compatible console logger"""
    import multiprocessing, logging
    logger = multiprocessing.get_logger()
    logger.setLevel(logging.WARNING)
    formatter = logging.Formatter('[%(asctime)s | %(levelname)s | %(name)s | %(processName)s] %(message)s')
    # handler = logging.FileHandler('logs/analysis.log', mode='a', encoding='UTF-8')
    handler = logging.StreamHandler(stream=sys.stdout)
    handler.setFormatter(formatter)

    if not len(logger.handlers):
        logger.addHandler(handler)
    return logger


def timer(f):
    """ Logs the time taken by the decorated function to run."""
    @wraps(f)
    def wrap(*args, **kw):
        logger = get_console_logger()
        logger.warning(f">> [{f.__name__}] Start")
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()
        logger.warning(f">> [{f.__name__}] Time Taken: {te - ts:.4f}")
        return result

    return wrap


if __name__ == "__main__":
    help(get_console_logger)
