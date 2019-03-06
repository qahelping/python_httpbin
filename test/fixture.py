import allure
import pytest
import logging
import logging.config

from allure_commons.types import AttachmentType

from config import dictLogConfig, file_name
from httpbin import HttpBin


@pytest.fixture(scope="function")
@pytest.mark.asyncio
async def prepare_for_test():
    httpbin = HttpBin()
    yield httpbin
    await httpbin.close()


@pytest.fixture(scope="function")
def logger():
    logging.config.dictConfig(dictLogConfig)
    logger = logging.getLogger("test")
    allure.attach.file(file_name, 'LOG')
    return logger
