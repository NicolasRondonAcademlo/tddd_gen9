import unittest


def addition(*args):
    a1, a2 = args
    return a1 + a2


# Hemos modificado addition para aceptar
# muchos argumentos  que pasa si envio 3 o si no enviamos alguno
class AdditionTestCase(unittest.TestCase):
    def test_three_args(self):
        result = addition(3, 2, 1)
        assert result == 6

    def test_no_args(self):
        result = addition()
        assert result == 0


if __name__ == '__main__':
    unittest.main()
