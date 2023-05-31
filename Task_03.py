# Генератор чисел Фибоначчи
# Последовательность Фибоначчи - 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

# Множество для проверки генерации рядов Фибоначчи
FIB_SET = (5, 8, 10, 15)


def fib_gen(n: int) -> list[int]:
    """Генератор чисел Фибоначчи"""
    fib_list = [0]
    fib1 = 0
    fib2 = 1
    for _ in range(n):
        fib_list.append(fib2)
        fib1, fib2 = fib2, fib2 + fib1
    yield fib_list


def main():
    for n in FIB_SET:
        print(*fib_gen(n))


if __name__ == "__main__":
    main()
