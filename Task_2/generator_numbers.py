import re
from typing import Callable


def generator_numbers(text: str):
   #  дійсні числа у тексті, які можуть містити десяткову частину або бути цілими числами
    pattern = re.compile(r"\b\d+(?:\.\d+)?\b")
   #  пошук у тексті чисел, які відповідають шаблону
    matches = pattern.finditer(text)
    for match in matches:
      #   повернення числа з тексту як число з плаваючою комою
        yield float(match.group())


def sum_profit(text: str, func: Callable):
    total_income = 0
    for number in func(text):
        total_income += number
    return total_income


text = """Загальний дохід працівника складається з
декількох частин: 1000.01 як основний дохід,
доповнений додатковими надходженнями 27.45 і 324.00 доларів."""

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
