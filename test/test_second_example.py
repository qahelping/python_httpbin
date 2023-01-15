import allure
import pytest


@pytest.mark.asyncio
@allure.feature("Second example")
async def test_second_example():
    with allure.step("Second example"):
        assert 1 + 2 == 3
