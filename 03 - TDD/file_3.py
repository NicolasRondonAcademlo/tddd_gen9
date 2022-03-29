import unittest


# Ahora que  nuesto test esta funcionando podemos revisar y refactorizar nuestra funcion
def addition(*args):
    a1, a2 = args
    return a1 + a2

# Si nuesto test aun funciona significa que no hemos cambiado el comportamiento


class AdditionTestCase(unittest.TestCase):
    def test_main(self):
        result = addition(3, 2)
        assert result == 5


if __name__ == '__main__':
    unittest.main()

