import time

def wait_for_fps(log_path,timeout=20):
    start = time.time()
    while time.time() - start < timeout:
        content = open(log_path).read()
        if "fps" in content :
            return True
        time.sleep(1)
    return False