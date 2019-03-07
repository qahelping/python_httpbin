import logging
import logging.config
import allure
import pytest
from config import dict_log_config, file_name_for_logging
from httpbin import HttpBin


@pytest.fixture(scope="function")
@pytest.mark.asyncio
async def prepare_for_test():
    """
    Fixture for create and close user session.
    """
    httpbin = HttpBin()
    yield httpbin
    await httpbin.close()


@pytest.fixture(scope="function")
def logger():
    """
    Fixture for logging.
    """
    logging.config.dictConfig(dict_log_config)
    logger = logging.getLogger("test")
    allure.attach.file(file_name_for_logging, 'LOG')
    return logger
