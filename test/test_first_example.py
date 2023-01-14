import allure
import pytest


@pytest.mark.asyncio
@allure.feature("First example")
async def test_first_example():
    with allure.step("First example"):
        assert 1+2 == 3

