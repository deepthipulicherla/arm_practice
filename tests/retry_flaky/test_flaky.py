import random
import allure
import pytest

#reruns 2 times if it fails with a gap of 5seconds
@pytest.mark.flaky(reruns=2,reruns_delay=5)
@allure.title("Flaky test")
@allure.description("Validates the flaky test by performing rerun for 2 times with a periodic gap of 5 seconds")
@allure.severity(allure.severity_level.CRITICAL)
def test_flaky(gpu_env):
    assert random.choice([True,False])