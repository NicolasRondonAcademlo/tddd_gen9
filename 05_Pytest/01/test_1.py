# Incluso podemos implementar clases sin heredar de TestCase
# Es importante que el nombre de la clase empiece por test

class TestMultiple:
    def test_first(self):
        assert 5 == 5
    def test_second(self):
        assert 10 == 10

# con pytest tambien podemos hacer uso de la bandera -k
#pytest -v -k first

# incluso sirve para exluir test
#pytest -v -k "not something"