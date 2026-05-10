import allure
import pytest
from utils.config_loader import config_loader
from workloads.fake_workload import run_workload
from utils.validation.performance import validate_fps

@allure.title("Config driven workloads")
@allure.description("Validates the config driven workloads")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_config(gpu_env):
    confs = config_loader()
    for w in confs:
        assert validate_fps(run_workload(w))

