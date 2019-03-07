from test.fixture import logger, prepare_for_test

import allure
import pytest


@pytest.mark.asyncio
@allure.feature("Testing headers")
async def test_headers(prepare_for_test, logger):
    """
    Test endpoint /response-headers.
    :param prepare_for_test:
    :param logger:
    """
    freeform = "application/json"
    httpbin = prepare_for_test
    with allure.step("Post headers " + freeform):
        response = await httpbin.post_response_headers(freeform)
        logger.info(response)
        assert response.status == 200
        assert response.headers["freeform"] == freeform
