# Самый длинный фильм
def longest_film(film_1: str, film_2: str,film_3: str) -> bool:
    # Напишите ваш код здесь
    return max(film_1, film_2, film_3, key=len)


if __name__ == '__main__':
    assert longest_film('Аладин', 'Мадагаскар', 'Бетховен') == 'Мадагаскар'
    assert longest_film('Железный Человек', 'Стражи Галактики', 'Капитан Америка') == 'Железный Человек'
    assert longest_film('Бумер', 'Бумер: Фильм второй', 'Бумеранг') == 'Бумер: Фильм второй'
    assert longest_film('Гарри Поттер и философский камень', 'Пираты Карибского моря: На странных берегах',
                        'ВАЛЛ·И') == 'Пираты Карибского моря: На странных берегах'
    assert longest_film('Ирония судьбы, или С легким паром!', 'Иван Васильевич меняет профессию ',
                        'Джентльмены удачи а') == 'Ирония судьбы, или С легким паром!'
    print("\nОтличная работа, отправляйте на проверку!")

# Количество слов
def list_of_numbers(n: int) -> list:
    # Напишите ваш код здесь
    return list(range(1, n + 1))


if __name__ == '__main__':
    assert list_of_numbers(1) == [1]
    assert list_of_numbers(5) == [1, 2, 3, 4, 5]
    assert list_of_numbers(9) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("\nОтличная работа, отправляйте на проверку!")


# Кто дальше?

hare_distances = [8, 5, 3, 2, 0, 1, 1]

turtle_distances = [3, 3, 3, 3, 3, 3, 3]

def solve(hare_distances: list, turtle_distances: list):
    hare_all = sum(hare_distances) # подсчитайте общую дистанцию зайца
    turtle_all = sum(turtle_distances) # подсчитайте общую дистанцию черепахи
    # определите, кто из двоих прошел бОльшую дистанцию
    if hare_all > turtle_all:
        result = "заяц"
    elif hare_all < turtle_all:
        result = "черепаха"
    else:
        result = "одинаково"
    return result

if __name__ == '__main__':
    # Этот код менять не надо
    result = solve([8, 5, 3, 2, 0, 1, 1], [3, 3, 3, 3, 3, 3, 3])
    assert result == "черепаха", f"Победитель определен неверно: {result}"
    print(f"Победитель: {result}")
    result = solve([8, 5, 3, 2, 2, 1, 1], [3, 3, 3, 3, 3, 3, 3])
    assert result == "заяц", f"Победитель определен неверно: {result}"
    print(f"Победитель: {result}")
    result = solve([8, 5, 3, 2, 1, 1, 1], [3, 3, 3, 3, 3, 3, 3])
    assert result == "одинаково", f"Победитель определен неверно: {result}"
    print(f"Победитель: {result}")