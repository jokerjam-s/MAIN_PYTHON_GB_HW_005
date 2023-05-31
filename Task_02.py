# Напишите однострочный генератор словаря, который принимает на вход три списка
# одинаковой длины: имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии

# Списки для проверки работы генератора
NAMES = ["Иван", "Петр", "Михаил", "Сергей"]
RATES = [10_000, 20_000, 15_000, 30_000]
PERCENTS = ["10.25%", "15.00%", "6.50%", "12.75%"]


def gen_dict(names: list[str], rates: list[int], percents: list[str]):
    """Генератор премий"""
    yield {d[0]: d[1] for d in
           list(map(lambda y: (y[0], y[1] * y[2] / 100), zip(names, rates, map(lambda x: float(x[:-1]), percents))))}


def main():
    print(NAMES)
    print(RATES)
    print(PERCENTS)
    print(*gen_dict(NAMES, RATES, PERCENTS))


if __name__ == "__main__":
    main()
