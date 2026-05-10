import allure
import pytest

from workloads.fake_workload import  run_workload
import json

@pytest.mark.regression
@allure.title("Performance test")
@allure.description("Validates vulken_rotate_triangle")
@allure.severity(allure.severity_level.CRITICAL)
def test_performance(gpu_env):
    fps = run_workload("vulken_rotate_triangle")
    data = json.load(open("baselines/vulken_rotate_triangle.json"))
    assert fps>=data["fps"]*0.95

