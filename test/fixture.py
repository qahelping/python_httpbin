import allure
import pytest
import logging
import logging.config

from allure_commons.types import AttachmentType

from httpbin import HttpBin


@pytest.fixture(scope="function")
@pytest.mark.asyncio
async def prepare_for_test():
    httpbin = HttpBin()
    yield httpbin
    await httpbin.close()


@pytest.fixture(scope="function")
def logger():
    file_name = "tests.log"
    dictLogConfig = {
        "version": 1,
        "handlers": {
            "fileHandler": {
                "class": "logging.FileHandler",
                "formatter": "myFormatter",
                "filename": file_name
            }
        },
        "loggers": {
            "test": {
                "handlers": ["fileHandler"],
                "level": "INFO",
            }
        },
        "formatters": {
            "myFormatter": {
                "format": "%(asctime)s - %(levelname)s - %(message)s"
            }
        }
    }

    logging.config.dictConfig(dictLogConfig)
    logger = logging.getLogger("test")
    allure.attach.file("./" + file_name, 'LOG')
    return logger
