

def caching_fibonacci():
    # Створюємо словник для зберігання значень чисел Фібоначчі
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            # якщо число вже є в кеші, повертаємо його
            return cache[n]
        else:
            # додаємо в кеш суму двох попередніх чисел
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]

    return fibonacci


# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі

# Виведе 55 cache {2: 1, 3: 2, 4: 3, 5: 5, 6: 8, 7: 13, 8: 21, 9: 34, 10: 55}
print(fib(10))
# Виведе 610 cache {....11: 89, 12: 144, 13: 233, 14: 377, 15: 610}
print(fib(15))
