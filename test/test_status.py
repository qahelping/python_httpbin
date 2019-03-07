from test.fixture import logger, prepare_for_test

import allure
import pytest


@pytest.mark.asyncio
@allure.feature("Testing status")
@pytest.mark.parametrize("code", [200, 300, 400, 500])
async def test_status(code, prepare_for_test, logger):
    """
    Test endpoint /status/:code.
    :param code: code
    :param prepare_for_test:
    :param logger:
    :return:
    """
    httpbin = prepare_for_test
    with allure.step("Get status " + str(code)):
        response = await httpbin.get_status(str(code))
        logger.info(response)
        assert response.status == code
        await httpbin.close()
