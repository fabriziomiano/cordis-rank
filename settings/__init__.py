import logging
from constants import (
    BUDGET_COLUMN_NAME, COMPANY_NAME, COMPANY_COLUMN_NAME,
    ACTIVITY_COLUMN_NAME, APPLY_ACTIVITY_FILTER, ACTIVITY_TYPE_FILTER,
    DEFAULT_URL, DEFAULT_LOCAL_DATA_PATH, COUNTRY_COLUMN_NAME
)


def get_logger(name):
    """
    Return a logger object of a given name
    :param name: str: logger name
    :return: logging.Logger object
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


def print_configuration():
    """Print the current settings based on constants.py"""
    configlog.info("-" * 50)
    configlog.info("Initializing with the following configuration")
    configlog.info("Check constants.py to change any of the following")
    configlog.info("-" * 50)
    configlog.info("COMPANY_NAME: {}".format(COMPANY_NAME))
    configlog.info("ACTIVITY_TYPE_FILTER: {}".format(ACTIVITY_TYPE_FILTER))
    configlog.info("APPLY_ACTIVITY_FILTER: {}".format(APPLY_ACTIVITY_FILTER))
    configlog.info("-" * 50)
    configlog.info("Assuming an input dataset with the following features")
    configlog.info("-" * 50)
    configlog.info("BUDGET_COLUMN_NAME: {}".format(BUDGET_COLUMN_NAME))
    configlog.info("COMPANY_COLUMN_NAME: {}".format(COMPANY_COLUMN_NAME))
    configlog.info("ACTIVITY_COLUMN_NAME: {}".format(ACTIVITY_COLUMN_NAME))
    configlog.info("COUNTRY_COLUMN_NAME: {}".format(COUNTRY_COLUMN_NAME))
    configlog.info("-" * 50)
    configlog.info("Fallback data sources")
    configlog.info("-" * 50)
    configlog.info("DEFAULT_URL: {}".format(DEFAULT_URL))
    configlog.info("DEFAULT_LOCAL_DATA_PATH: {}".format(DEFAULT_LOCAL_DATA_PATH))
    configlog.info("-" * 50)


datalog = get_logger(name="data_tools")
datalog.setLevel(logging.INFO)

printerlog = get_logger(name="printer")
printerlog.setLevel(logging.INFO)

configlog = get_logger(name="config")
configlog.setLevel(logging.INFO)
