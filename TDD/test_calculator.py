from .main import SimpleCalculator


def test_add_two_numbers():
    calculator = SimpleCalculator()
    result = calculator.add(4,5)
    assert result == 9

def test_add_three_numbers():
    calculator = SimpleCalculator()
    result = calculator.add(4,5,6)
    assert result == 15

def test_add_many_numbers():
    numbers = range(100)
    calculaotr = SimpleCalculator()
    result = calculaotr.add(*numbers)
    assert result == 4950