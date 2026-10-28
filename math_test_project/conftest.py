# conftest.py
import pytest
import sys
import os

# Добавляем корневую директорию в путь, чтобы импортировать math_operations
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from math_operations import add_numbers

@pytest.fixture
def add_func():
    """
    Фикстура для подготовки тестового окружения.
    Возвращает функцию сложения для использования в тестах.
    """
    return add_numbers