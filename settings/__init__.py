import logging


def get_logger(name):
    """
    Return a logger object of a given name
    :param name: str: logger name
    :return: logging.getLogger object
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.propagate = 1  # propagate to parent
        console = logging.StreamHandler()
        logger.addHandler(console)
        formatter = logging.Formatter(
            '%(name)s - [%(levelname)s] - %(message)s')
        console.setFormatter(formatter)
    return logger


datalog = get_logger(name="data_tools")
datalog.setLevel(logging.INFO)

printerlog = get_logger(name="printer")
printerlog.setLevel(logging.INFO)
