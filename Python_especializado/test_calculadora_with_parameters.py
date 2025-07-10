#Las pruebas unitarias parametrizadas, son pruebas las cuales pueden recibir multiples valores

from calculator import sum, rest, multiply, divide
import pytest

#Test para las funciones de calculator
def test_sum(num1,num2, expected_result):
  assert sum(num1,num2) == expected_result
  
def test_rest():
  assert rest(1,2) == -1
  
def test_multiply():
  assert multiply(1,2) == 2
  
def test_divide():
  assert divide(1,2) == 0.5
  
def test_divide_by_zero():
  with pytest.raises(ValueError):
    divide(1,0)
