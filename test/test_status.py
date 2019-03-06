import allure
import pytest

from test.fixture import prepare_for_test, logger


@pytest.mark.asyncio
@allure.feature("Testing status")
@pytest.mark.parametrize("code", [200, 300, 400, 500])
async def test_status(code, prepare_for_test, logger):
    httpbin = prepare_for_test
    with allure.step("Get status " + str(code)):
        response = await httpbin.get_status(str(code))
        logger.info(response)
        assert response.status == code
        await httpbin.close()
