from test.fixture import logger, prepare_for_test
import allure
import pytest
from config import redirect_url


@pytest.mark.asyncio
@allure.feature("Testing redirect")
async def test_redirect(prepare_for_test, logger):
    """
    Test endpoint /redirect/:n.
    :param prepare_for_test: fixture create session
    :param logger: fixture logging
    """
    redirect_number = 5
    httpbin = prepare_for_test
    with allure.step("Redirect"):
        response, new_redirect_url = await httpbin.redirect(str(redirect_number))
        logger.info(response)
        amount_redirects = len(response.history)
        assert amount_redirects == redirect_number
        assert response.status == 200
        assert new_redirect_url == redirect_url
        for item in range(amount_redirects):
            assert response.history[item].status == 302
