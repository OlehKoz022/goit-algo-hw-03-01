# Завдання № 2
from random import randint
# Параметри функції
min = 1
max = 100
quantity = 6

def get_numbers_ticket(min, max, quantity):
    lottery_numbers = set()                  # Створюємо множину
    while len(lottery_numbers) != quantity:  # Використовуємо цикл 
        lottery_numbers.add(randint(min, max))
    return lottery_numbers                   # Повертаємо відсортований список

print(sorted(list(get_numbers_ticket(min, max, quantity)))) # Сортуємо і перетворюємо множину в список