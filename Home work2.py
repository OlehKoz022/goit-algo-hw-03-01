# Завдання №1
from datetime import datetime, timedelta, date

date_one = "2025-02-25" 

def get_days_from_today(date_one):  # Створюємо функцію для розрахунку днів між заданою і поточною датою
    date_one = datetime.strptime(date_one, "%Y-%m-%d") # Перетворюємо рядок date_one у об*єкт datetime
    date_today = datetime.today() # Визначаємо поточну дату
    difference_day = date_one - date_today # РОзрахунок різниці між заданою датою і поточною
    difference_day = difference_day.days # Переводимо різницю у днях в ціле число
    return difference_day


print(get_days_from_today(date_one))