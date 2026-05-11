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
        """Kill subprocess if available. Threads cannot be killed."""
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
                if "GPU HANG" in open(self.log_path).read():
                    self.error = "GPU HANG DETECTED"
                    self._safe_kill()
                    break
            except FileNotFoundError:
                pass

            time.sleep(0.2)

    def start(self):
        t = threading.Thread(target=self.monitor)   # FIXED
        t.daemon = True
        t.start()
        return t
