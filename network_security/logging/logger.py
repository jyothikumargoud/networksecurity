import os
from datetime import datetime
import logging

#create a log file format
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

#crete a log path file called logs
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)

# if that logs file alresy exist not create buy using Exist_ok = True
os.makedirs(logs_path,exist_ok=True)
LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


