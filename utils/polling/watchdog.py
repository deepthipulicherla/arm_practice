import time
import threading

class watchdog:

    def __init__(self, process, log_path, timeout=20):
        self.process = process
        self.log_path = log_path
        self.timeout = timeout
        self.stopflag = False
        self.error = None

    def _safe_kill(self):
        if hasattr(self.process, "kill"):
            self.process.kill()

    def monitor(self):
        start = time.time()

        while not self.stopflag:
            # timeout
            if time.time() - start > self.timeout:
                self.error = "Timeout"
                self._safe_kill()
                break

            # GPU hang
            try:
                with open(self.log_path, "r") as f:
                    if "GPU HANG" in f.read():
                        self.error = "GPU HANG DETECTED"
                        self._safe_kill()
                        break
            except FileNotFoundError:
                pass

            time.sleep(0.1)

    def start(self):
        t = threading.Thread(target=self.monitor)
        t.daemon = False
        t.start()
        return t
