import pytest


def pytest_addoption(parser):
    parser.addoption("--name", action="store", default="default name")


@pytest.fixture(scope="session")
def name(pytestconfig):
    return pytestconfig.getoption("name")
