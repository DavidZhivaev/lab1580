def get_declension(number, forms):
    """
    Возвращает правильную форму слова в зависимости от числа.
    Список из 3 вариантов: множественное (5-20), единственное (1), родительный (2-4)
    Пример для минут: ["минут", "минута", "минуты"]
    """
    # Исключения для чисел от 11 до 19
    if 11 <= number % 100 <= 19:
        return forms[0]

    # Получаю последнюю цифру для определения окончаниЯ
    last_digit = number % 10
    
    if last_digit == 1:
        return forms[1]
    elif 2 <= last_digit <= 4:
        return forms[2]
    else:
        return forms[0]

def main():
    try:
        # Просим ввести данные
        user_input = input().split()
        
        # Проверяю, два ли аргумента
        if len(user_input) != 2:
            raise ValueError("Неверный формат ввода")

        hours = int(user_input[0])
        minutes = int(user_input[1])

        # Проверка, подходят ли данные под условие
        if not (0 <= hours <= 23):
            print("Введены недопустимые данные: часы должны быть от 0 до 23.")
            return
        if not (0 <= minutes <= 59):
            print("Введены недопустимые данные: минуты должны быть от 0 до 59.")
            return

        # Полночь и полдень
        if hours == 0 and minutes == 0:
            print("полночь")
            return
        if hours == 12 and minutes == 0:
            print("полдень")
            return

        # Определение времени суток, окончание фразы
        if 0 <= hours <= 5:
            time_of_day = "ночи"
        elif 6 <= hours <= 11:
            time_of_day = "утра"
        elif 12 <= hours <= 17:
            time_of_day = "дня"
        else: # 18 <= hours <= 23
            time_of_day = "вечера"

        # Преобразование в 12-часовой формат для вывода чисел
        # 0 -> 12 (ночь), 13 -> 1
        display_hours = hours % 12
        if display_hours == 0:
            display_hours = 12

        # Склонение слов, джля правильного вывода
        # Формы: множественное (5, 0), единственное (1), родительный (2-4)
        hour_word = get_declension(display_hours, ["часов", "час", "часа"])
        minute_word = get_declension(minutes, ["минут", "минута", "минуты"])

        # Преобразовываю результат в нужный формат
        result = f"{display_hours} {hour_word}"
        
        if minutes > 0:
            result += f" {minutes} {minute_word}"
        else:
            # Если минуты 00, то добавляю ровно
            result += " ровно"
            
        result += f" {time_of_day}"
        
        print(result)

    except ValueError:
        # Обработка случая, если введены не числа
        print("Ошибка ввода: пожалуйста, введите два целых числа.")

if __name__ == "__main__":
    main()
