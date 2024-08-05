# -*- coding: utf-8 -*-
"""
Напишите однострочный генератор словаря, который принимает на вход три списка
одинаковой длины: имена str, ставка int, премия str с указанием процентов
вида 10.25%.
В результате result получаем словарь с именем в качестве ключа и суммой премии
в качестве значения.
"""

import logging
import sys

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_bonus(names, salaries, bonuses):
    try:
        if not (len(names) == len(salaries) == len(bonuses)):
            raise ValueError("Все списки должны быть одинаковой длины")
        
        result = {name: sal * float(bon.strip('%')) / 100 for name, sal, bon in zip(names, salaries, bonuses)}
        logging.info(f"Рассчитанные премии: {result}")
        return result
    except Exception as e:
        logging.error(f"Ошибка при расчете премий: {e}")
        return None

if __name__ == "__main__":
    try:
        # Получение параметров из командной строки
        
        names = sys.argv[1].split(',')
        salaries = list(map(int, sys.argv[2].split(',')))
        bonuses = sys.argv[3].split(',')

        logging.info(f"Получены данные: имена - {names}, ставки - {salaries}, премии - {bonuses}")

        # Вызов функции calculate_bonus
        result = calculate_bonus(names, salaries, bonuses)

        if result:
            print(result)
    except Exception as e:
        logging.error(f"Ошибка при обработке командной строки: {e}")
        print("Использование: python script.py 'name1,name2,...' 'salary1,salary2,...' 'bonus1%,bonus2%,...'")
