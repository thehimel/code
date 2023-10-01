"""Author: Himel Das"""

import logging

# Configure the logging settings
logging.basicConfig(
    level=logging.INFO,  # Set the minimum log level (e.g., DEBUG, INFO, WARNING, ERROR)
    format="%(asctime)s [%(levelname)s] %(message)s",  # Define the log message format
    datefmt="%Y-%m-%d %H:%M:%S",  # Define the date and time format
)

# Create the logger instance
logger = logging.getLogger("core_logger")
