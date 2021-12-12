import functools

import numpy as np
from numpy.typing import NDArray

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def paint_and_count(matrix: NDArray[int], row_index: int, col_index: int):
    if matrix[row_index][col_index] == 9:
        return 0
    matrix[row_index][col_index] = 9
    count = 1
    for direction in directions:
        count += paint_and_count(matrix, row_index + direction[0], col_index + direction[1])
    return count


def day_9_1(matrix: NDArray[int]):
    summed = 0

    for row_index in range(1, len(matrix) - 1):
        for col_index in range(1, len(matrix[row_index]) - 1):
            current_el = matrix[row_index][col_index]
            neighbors = [matrix[row_index + direction_tuple[0]][col_index + direction_tuple[1]] for direction_tuple in
                         directions]
            if current_el not in neighbors and current_el <= min(neighbors):
                summed += current_el + 1
    return summed


def day_9_2(matrix: NDArray[int]):
    count = []

    for row_index in range(len(matrix)):
        for col_index in range(len(matrix[row_index])):
            if matrix[row_index][col_index] != 9:
                count.append(paint_and_count(matrix, row_index, col_index))

    count = np.array(count)

    index = np.argpartition(count, -3)[-3:]

    return functools.reduce(lambda a, b: a * b, count[index])


def day_9(part: int = 1):
    with open('../input.txt', 'r') as input_file:
        matrix = np.array([[int(el) for el in line.strip()] for line in input_file.readlines()])

    matrix = np.pad(matrix, 1, constant_values=9)

    return day_9_1(matrix) if part == 1 else day_9_2(matrix)


if __name__ == '__main__':
    print(day_9(part=1))
    print(day_9(part=2))
