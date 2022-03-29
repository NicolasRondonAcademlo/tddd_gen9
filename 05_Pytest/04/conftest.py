import pytest


@pytest.fixture(scope="session", autouse=True)
def setupsuite():
    print("STARTING TESTS")
    yield
    print("FINISHED TESTS")


# correr test pytest -s

# Imaginemos que queremos acceder a un numero ramdom a traves de una peticion http
@pytest.fixture
def random_number_generator():
    import random
    
    def _number_provider():
        return random.choice(range(10))
    yield _number_provider
