import logging
from settings import get_logger


def test_get_logger():
    """Test get_logger()"""
    test_logger = get_logger("test_logger")
    assert type(test_logger) == logging.Logger
    assert test_logger.name == "test_logger"
