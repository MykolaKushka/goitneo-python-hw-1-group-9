from datetime import datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    # Створюємо словник для зберігання імен користувачів по днях тижня
    birthdays_per_week = defaultdict(list)

    # Отримуємо поточну дату
    today = datetime.today().date()

    # Визначаємо початок тижня (понеділок)
    monday = today - timedelta(days=today.weekday())

    # Перевіряємо, чи поточний рік є високосним
    leap_year = today.year % 4 == 0 and (today.year % 100 != 0 or today.year % 400 == 0)

    # Перебираємо користувачів
    for user in users:
        # Отримуємо дані про користувача
        name = user["name"]
        birthday = user["birthday"].date()

        # Визначаємо день народження для цього року
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо день народження вже пройшов у цьому році, додаємо рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Визначаємо різницю в днях між сьогоднішньою датою і днем народження
        delta_days = (birthday_this_year - today).days

        # Якщо день народження випадає на наступний тиждень, зберігаємо його
        if 0 <= delta_days < 7:
            # Визначаємо день тижня дня народження
            birthday_weekday = (monday + timedelta(days=delta_days)).strftime("%A")

            # Якщо день народження випадає на вихідний, зберігаємо його на понеділок
            if birthday_this_year.weekday() >= 5:
                birthday_weekday = "Monday"

            # Додаємо ім'я користувача до відповідного дня тижня
            birthdays_per_week[birthday_weekday].append(name)

    # Виводимо список користувачів по днях тижня
    for day, users in birthdays_per_week.items():
        print(f"{day}: {', '.join(users)}")

# Приклад використання функції
users = [
    {"name": "John", "birthday": datetime(1990, 5, 20)},
    {"name": "Jane", "birthday": datetime(1985, 10, 15)},
    {"name": "Alex", "birthday": datetime(1978, 3, 9)},
    {"name": "Kate", "birthday": datetime(1995, 8, 10)},
    {"name": "Michael", "birthday": datetime(2000, 3, 5)},
]

get_birthdays_per_week(users)
