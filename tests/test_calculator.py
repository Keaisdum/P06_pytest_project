from calculator.calculator import Calculator
import pytest
class TestCalculator:
 def test_add(self):
    # arrange
    a = 4321
    b = 1234
    cal = Calculator()
    # act
    result = cal.add(a, b)
    # assert
    expected = 5555
    assert result == expected
 def test_subtract(self):
   # arrange
    a = 4321
    b = 1234
    cal = Calculator()
    # act
    result = cal.subtract(a, b)
    # assert
    expected = 3087
    assert result == expected
 def test_mult(self):
   # arrange
    a = 4
    b = 4
    cal = Calculator()
    # act
    result = cal.multiply(a, b)
    # assert
    expected = 16
    assert result == expected

 def test_div(self):
   # arrange
    a = 4
    b = 4
    b2 = 0
    cal = Calculator()
    # act
    result = cal.divide(a, b)
    # assert
    expected = 1
    assert result == expected
    with pytest.raises(ZeroDivisionError):
            cal.divide(a, b2)