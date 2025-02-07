import logging
import os
import sys
from datetime import datetime  # Import datetime

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log"
logs_dir = os.path.join(os.getcwd(), 'logs')  # Create the logs directory
os.makedirs(logs_dir, exist_ok=True)  # Ensure the logs directory exists

LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)  # Set full log file path

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)d - %(levelname)s - %(message)s',
    level=logging.INFO,
)

logging.info("Logging is successfully set up!")  # Test log message
