import pytest

@pytest.fixture(scope="function", autouse=True)
def enterexit():
    print("ENTER")
    yield
    print("EXIT")