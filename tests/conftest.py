import os
import pytest
from utils.device_capabilities import dev_caps
from utils.logger import init_logger
import logging

def pytest_sessionstart(session):
    init_logger()
    logging.info("Pytest session started")


#we simulate gpu driver as we dont have locally
@pytest.fixture(scope="session")
def gpu_env():
    #simulate gpu verison
    os.environ["GPU_DRIVER_VERSION"] = "1.0.0"
    #simulate clearing logs
    logging.info("GPU environment setup complete")
    yield
    logging.info("GPU environment cleanup complete")

@pytest.fixture(scope="session")
def caps():
    return dev_caps()

