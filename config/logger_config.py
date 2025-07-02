import logging
import sys

def setup_logger(name='system_monitor_logger'):
    """
    Sets up and returns a logger instance.

    Args:
        name (str): The name for the logger.

    Returns:
        logging.Logger: A configured logger instance.
    """
    # Create a logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Create a handler to write to the console (stdout)
    handler = logging.StreamHandler(sys.stdout)

    # Create a formatter and set it for the handler
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)

    # Add the handler to the logger
    # This check prevents adding duplicate handlers if the function is called multiple times
    if not logger.handlers:
        logger.addHandler(handler)

    return logger

# You can also create a default logger instance to be imported directly
log = setup_logger()