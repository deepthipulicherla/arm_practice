import logging
import os

def init_logger():
    os.makedirs("test_logs",exist_ok=True)
    logging.basicConfig(filename="test_logs/system.log",level=logging.INFO,format="%(asctime)s [%(levelname)s] %(message)s")

def get_workload_logger():
    os.makedirs("test_logs",exist_ok=True)
    logger = logging.getLogger("workload")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    if not logger.handlers:
        handler = logging.FileHandler("test_logs/workload.log")
        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger

