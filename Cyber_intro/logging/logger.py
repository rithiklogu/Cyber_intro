import logging
import os 
import sys
LOG_FILE = f'{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log'
logs_path = os.path.join(os.getcwd(), 'logs',LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)