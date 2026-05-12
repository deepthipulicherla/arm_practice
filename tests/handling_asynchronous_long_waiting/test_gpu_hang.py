import threading
import time
import pytest
from utils.polling.watchdog import watchdog
import allure

@allure.title("GPU HANG")
@allure.description("Gpu hang test simulation")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
@pytest.mark.skip(reason="Feature not supported yet")
def test_gpu_hang(tmp_path, gpu_env):
    log_file = tmp_path / "system.log"
    log_file.write_text("")

    #simple workload (just sleeps)
    def workload():
        time.sleep(5)

    t = threading.Thread(target=workload)
    t.start()

    #write GPU HANG after 1 sec
    def inject_hang():
        time.sleep(1)
        with open(log_file,'a') as f:
            f.write("GPU HANG\n")

    threading.Thread(target=inject_hang).start()

    wd = watchdog(t,str(log_file),timeout=10)
    t_wd = wd.start()

    t.join()
    wd.stopflag =  True
    t_wd.join()

    assert wd.error == "GPU HANG DETECTED"







