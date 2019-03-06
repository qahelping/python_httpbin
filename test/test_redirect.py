import allure
import pytest

from httpbin import HttpBin
from test.fixture import prepare_for_test, logger

url = "https://httpbin.org/get"

@pytest.mark.asyncio
@allure.feature("Testing redirect")
async def test_redirect(prepare_for_test, logger):
    redirect_number = 5
    httpbin = prepare_for_test
    with allure.step("Redirect"):
        response, redirect_url = await httpbin.redirect(str(redirect_number))
        logger.info(response)
        assert response.status == 200
        assert redirect_url == url
        assert response.history[0].status == 302
        assert len(response.history) == redirect_number
