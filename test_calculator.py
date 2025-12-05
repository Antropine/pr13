"""
Тесты для калькулятора
"""

import pytest
from calculator import add, subtract, multiply, divide, power

class TestCalculator:
    """Класс с тестами для всех функций калькулятора"""

    def test_add_positive_numbers(self):
        """Тест сложения положительных чисел"""
        assert add(2, 3) == 5
        assert add(10, 20) == 30
        assert add(0.5, 0.5) == 1.0

    def test_add_negative_numbers(self):
        """Тест сложения отрицательных чисел"""
        assert add(-5, -3) == -8
        assert add(-10, 5) == -5

    def test_subtract(self):
        """Тест вычитания"""
        assert subtract(10, 5) == 5
        assert subtract(5, 10) == -5
        assert subtract(0, 5) == -5

    def test_multiply(self):
        """Тест умножения"""
        assert multiply(3, 4) == 12
        assert multiply(-2, 5) == -10
        assert multiply(0, 100) == 0

    def test_divide(self):
        """Тест деления"""
        assert divide(10, 2) == 5
        assert divide(9, 3) == 3
        assert divide(7, 2) == 3.5

    def test_divide_by_zero(self):
        """Тест деления на ноль (должно вызвать исключение)"""
        with pytest.raises(ValueError, match="Деление на ноль невозможно"):
            divide(10, 0)

    def test_power(self):
        """Тест возведения в степень"""
        assert power(2, 3) == 8
        assert power(5, 2) == 25
        assert power(10, 0) == 1
        assert power(2, -1) == 0.5

    def test_add_large_numbers(self):
        """Тест сложения больших чисел"""
        assert add(1000000, 2000000) == 3000000

    def test_multiply_by_zero(self):
        """Тест умножения на ноль"""
        assert multiply(999, 0) == 0
        assert multiply(0, 999) == 0
