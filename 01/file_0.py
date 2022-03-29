# Escribir una pieza de código que testea una parte del software
# Dividimos el programa en pequeñas islas que vamos a testear y cada isla es un test case

# Python trae el modulo unittest
# https://docs.python.org/3/library/unittest.html
import unittest


class MyTestCase(unittest.TestCase):
    def test_one(self):
        pass

# si corremos python3 test_0.py no pasara nada necesitamos ejecutarlo

if __name__ == '__main__':
    unittest.main()

# Si queremeos conocer que test corrimos podemos agregar la bandera -v
# python3 test_0.py -v

