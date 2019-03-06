import allure
import pytest

from config import redirect_url
from test.fixture import prepare_for_test, logger

@pytest.mark.asyncio
@allure.feature("Testing redirect")
async def test_redirect(prepare_for_test, logger):
    redirect_number = 5
    httpbin = prepare_for_test
    with allure.step("Redirect"):
        response, new_redirect_url = await httpbin.redirect(str(redirect_number))
        logger.info(response)
        count_redirects = len(response.history)
        assert count_redirects == redirect_number
        assert response.status == 200
        assert new_redirect_url == redirect_url
        for item in range(count_redirects):
            assert response.history[item].status == 302