import time
import random
from utils.logger import get_workload_logger

#simulate gpu workload by validating fps
def run_workload(name):
    time.sleep(1)
    #validate fps
    fps = random.randint(50,120)
    log = get_workload_logger()
    log.info(f"Workload : {name}")
    log.info(f"FPS : {fps}")
    return fps
