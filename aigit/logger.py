from loguru import logger
import sys

def setup_logger(verbose):
    logger.remove()
    logger.add(sys.stderr, level="DEBUG" if verbose else "INFO")

log = logger