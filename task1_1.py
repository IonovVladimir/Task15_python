# -*- coding: utf-8 -*-
"""
Напишите функцию для транспонирования матрицы transposed_matrix, принимает в
аргументы matrix, и возвращает транспонированную матрицу.
"""

import logging
import sys

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
        
        # Дополнительная проверка, что все строки матрицы имеют одинаковую длину
        if any(len(row) != cols for row in matrix):
            logging.error("Все строки в матрице должны иметь одинаковое количество столбцов")
            return None
        
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

def form_matrix(matrix_str):
    try:
        matrix = [
            [int(num) for num in row.split(",")]
            for row in matrix_str.strip().split(";")
        ]
        return matrix
    except Exception as e:
        logging.error(f"Ошибка при формировании матрицы: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        logging.error("Необходимо передать один аргумент (строковое представление матрицы)!!!")
        sys.exit(1)
    
    matrix_str = sys.argv[1]
    matrix = form_matrix(matrix_str)
    
    if matrix is None:
        logging.error("!Ошибка при формировании входной матрицы!")
        sys.exit(1)
    
    transposed = transpose(matrix)
    
    if transposed:
        for row in transposed:
            print(row)

#use python task1_1.py "1,2,3;4,5,6;7,8,9" to start