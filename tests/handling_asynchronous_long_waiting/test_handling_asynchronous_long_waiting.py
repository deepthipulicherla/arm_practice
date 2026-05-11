import allure
import pytest

from workloads.fake_workload import run_workload

@allure.title("asynchronous handling")
@allure.description("Handling asynchronous or long running test")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
@pytest.mark.skip(reason="Feature not supported yet")
@pytest.mark.timeout(20)
def test_heavy_workload():
    #if workload hangs pytest kills it(prevents infinite waiting)
    fps = run_workload("bigtime")
    assert fps > 0