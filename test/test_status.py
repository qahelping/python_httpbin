from test.fixture import logger, prepare_for_test
import allure
import pytest


@pytest.mark.asyncio
@allure.feature("Testing status")
@pytest.mark.parametrize("status", [200, 300, 400, 500])
async def test_status(status, prepare_for_test, logger):
    """
    Test endpoint /status/:code.
    :param status: status
    :param prepare_for_test: fixture create session
    :param logger: fixture logging
    """
    httpbin = prepare_for_test
    with allure.step("Get status " + str(status)):
        response = await httpbin.get_status(str(status))
        logger.info(response)
        assert response.status == status
        await httpbin.close()
