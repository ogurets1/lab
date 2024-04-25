def day_of_week(day_language):
    days_ru = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
    days_en = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day, language = day_language
    if language.lower() == 'русский':
        return days_ru[day - 1]
    elif language.lower() == 'английский':
        return days_en[day - 1]
    else:
        return "Неверно указан язык"

# Ввод списка с клавиатуры
day_language = list(input("Введите номер дня недели и язык (номер_дня язык): ").split())

# Вызов функции
print("Название дня недели:", day_of_week(day_language))