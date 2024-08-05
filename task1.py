# -*- coding: utf-8 -*-
"""
Напишите функцию для транспонирования матрицы transposed_matrix, принимает в
аргументы matrix, и возвращает транспонированную матрицу.
"""

import logging

# Настройка логгера
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def transpose(matrix):
    try:
        # Сообщение начала функции
        logging.info("Функция transpose была вызвана")
        
        # Проверка корректности входных данных
        if not matrix or not all(isinstance(row, list) for row in matrix):
            logging.error("Некорректный формат входной матрицы")
            return None
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Логирование размеров матрицы
        logging.info(f"Размеры матрицы: {rows}x{cols}")
        
        transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]
        
        for i in range(rows):
            for j in range(cols):
                transposed_matrix[j][i] = matrix[i][j]
        
        # Сообщение успешного завершения функции
        logging.info("Транспонирование завершено успешно")
        return transposed_matrix

    except Exception as e:
        # Логирование ошибок
        logging.error(f"Произошла ошибка: {e}")
        return None

# Тесто
'''matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix = [
    [1, 2],
    [4, 5, 6]
]


matrix = [
    ["a", 2, 3],
    [4, "z", 6]
]

matrix = "error_matrix"


transposed = transpose(matrix)
if transposed:
    for row in transposed:
        print(row)

no_matrix= 3.14
transposed = transpose(no_matrix)
if transposed:
    for row in transposed:
        print(row)

colums_or_rows = [[1, 2, 3]]  

transposed = transpose(colums_or_rows)
if transposed:
    for row in transposed:
        print(row)
'''        
matrix = [
    [1, 2, 3],
    [4, 5]
]

transposed = transpose(matrix)
if transposed:
    for row in transposed:
        print(row)