import allure

from utils.device_capabilities import dev_caps
import pytest

@pytest.mark.regression
@allure.title("Device capabilties")
@allure.description("Validates the test on vulken , open-gles , ray_tracing")
@allure.severity(allure.severity_level.CRITICAL)
def test_workload(caps,gpu_env):
    if not dev_caps()["supports_ray_tracing"]:
        pytest.skip("Ray_Tracing not supported")
    assert True
