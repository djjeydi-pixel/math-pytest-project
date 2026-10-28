# tests/test_addition.py
import pytest

# Кейс 1: Сложение двух простых положительных чисел
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (10, 25, 35),
    (100, 500, 600)
], ids=["small_numbers", "medium_numbers", "large_numbers"])
def test_add_two_positive(add_func, a, b, expected):
    """Тест сложения двух положительных чисел."""
    assert add_func(a, b) == expected

# Кейс 2: Сложение трех и более чисел с разными знаками
@pytest.mark.parametrize("numbers, expected", [
    ((-5, 10, -2), 3),
    ((100, -50, -25, 10), 35), # <-- Добавлены скобки вокруг чисел, ответ 35
    ((-1, -2, -3, 10, 4), 8)   # <-- Добавлены скобки, ответ 8
], ids=["three_numbers", "four_numbers", "five_numbers"])
def test_add_different_signs(add_func, numbers, expected):
    """Тест сложения трех и более чисел с разными знаками."""
    assert add_func(*numbers) == expected

# Кейс 3: Сложение нескольких чисел, включая нули
@pytest.mark.parametrize("numbers, expected", [
    ((0, 0, 0), 0),
    ((0, 5, 0, -3), 2),
    ((0, 10, 20, 0, -5, 25), 50)
], ids=["only_zeros", "with_zeros_and_negatives", "mixed_with_zeros"])
def test_add_with_zeros(add_func, numbers, expected):
    """Тест сложения чисел, включающих нули."""
    assert add_func(*numbers) == expected