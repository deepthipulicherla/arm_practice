import threading
import time
import pytest
import allure
from utils.polling.watchdog import watchdog

@allure.title("GPU TIMEOUT")
@allure.description("check for the gpu workoad timeout")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
#@pytest.mark.skip(reason="Feature not supported yet")
def test_watchdog_timeout(tmp_path, gpu_env):
    log_file = tmp_path / "system.log"
    log_file.write_text("")

    def long_workload():
        time.sleep(5)

    t = threading.Thread(target=long_workload)
    t.start()

    wd = watchdog(t, str(log_file), timeout=1)
    t_wd = wd.start()

    t.join(timeout=2)
    wd.stopflag = True
    t_wd.join(timeout=1)

    assert wd.error == "Timeout"

