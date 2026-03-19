import sys

def get_declension(number: int, forms: list[str]) -> str:
    """
    Функция для склонения существительных, из числительного.
    forms: ['час', 'часа', 'часов'] или ['минута', 'минуты', 'минут']
    """
    # Исключения для чисел от 11 до 14
    if 11 <= number % 100 <= 14:
        return forms[2]
    
    last_digit = number % 10
    if last_digit == 1:
        return forms[0]
    if 2 <= last_digit <= 4:
        return forms[1]
    return forms[2]

def get_time_description(hours: int, minutes: int) -> str:
    """
    Функция преобразует часы и минуты в текстовое описание времени.
    """
    # Сначала проверяем постоянные случаи ( полночь / полдень )
    if minutes == 0:
        if hours == 0:
            return "полночь"
        if hours == 12:
            return "полдень"

    # Определяем формат из часов для определения части дня
    if 0 <= hours < 6:
        period = "ночи"
    elif 6 <= hours < 12:
        period = "утра"
    elif 12 <= hours < 18:
        period = "дня"
    else:
        period = "вечера"

    # Преобразуем часы в 12-часовой формат
    # Если 0 часов ночи (не полночь), то "0 часов" или "12 часов"
    display_hours = hours % 12
    if display_hours == 0:
        # Для корректного склонения: 0 часов ночи или 12 часов дня
        display_hours = 12 if hours == 12 or hours == 0 else 0

    # Получаем правильные формы слов
    hour_word = get_declension(display_hours, ["час", "часа", "часов"])
    
    if minutes == 0:
        # Случай, когда минуты отсутствуют
        return f"{display_hours} {hour_word} {period} ровно"
    
    # Случай с минутами
    minute_word = get_declension(minutes, ["минута", "минуты", "минут"])
    return f"{display_hours} {hour_word} {minutes} {minute_word} {period}"

def validate_input(h_str: str, m_str: str) -> tuple[bool, str]:
    """
    Проверяет входные данные на соответствие типам и диапазонам.
    Возвращает ошибку или нужные нам данные..
    """
    try:
        h, m = int(h_str), int(m_str)
    except ValueError:
        return False, "Ошибка: введенные данные должны быть целыми числами."

    if not (0 <= h <= 23):
        return False, "Введены недопустимые данные: часы должны быть от 0 до 23."
    if not (0 <= m <= 59):
        return False, "Введены недопустимые данные: минуты должны быть от 0 до 59."
    
    return True, ""

def main():
    """
    Демонстрация функционала программы. 
    """
    raw_data = input("Введите время (часы и минуты через пробел): ").split()
    
    # Проверяем, ввел лти пользователь 2 аргумента
    if len(raw_data) != 2:
        print("Ошибка: требуется ввести два числа через пробел.")
        return

    # Распоковываем и проверяем данные
    is_valid, error_message = validate_input(raw_data[0], raw_data[1])
    
    if not is_valid:
        print(error_message)
        sys.exit(1)

    # Приведение к int после успешной проверки
    hours, minutes = int(raw_data[0]), int(raw_data[1])
    
    # Вычисление результата и вывод
    result = get_time_description(hours, minutes)
    print(result)

if __name__ == "__main__":
    # Точка входа
    main()
