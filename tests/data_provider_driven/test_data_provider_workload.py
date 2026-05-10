import allure
import pytest
from workloads.fake_workload import run_workload

@allure.title("Data driven testing")
@allure.description("Validate the gpu with mutilple workload datasets")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
@pytest.mark.parametrize('workload,fps',[("vulken_rotate_triangle",60),("open_gles_shadow",45)])
def test_data_provider(gpu_env,workload,fps):
    assert run_workload(workload)>=fps