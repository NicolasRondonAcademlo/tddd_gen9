import pytest


@pytest.fixture
def greetings():
    print("HELLO!")
    yield
    print("GOODBYE")


# Si en este momento ejecutamos no pasara nada

class TestMultiple:
    def test_first(self):
        assert 5 == 5

    @pytest.mark.usefixtures("greetings")
    def test_second(self):
        assert 10 == 10
# Si ahora ejecutamos pytest -s vemos que los prints si hacen antes y despues de la funcion