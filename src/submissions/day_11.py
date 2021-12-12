from collections import deque
from typing import Tuple, Deque, List

directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]


def day_11_calculate(matrix: List[List[int]], steps: int = 100, part: int = 1):
    total_flashes = 0
    for step in range(steps):
        step_flashes = 0
        flash_queue: Deque[Tuple[int, int]] = deque()
        for row_index in range(len(matrix)):
            for col_index in range(len(matrix[row_index])):
                if matrix[row_index][col_index] < 9:
                    matrix[row_index][col_index] += 1
                else:
                    flash_queue.append((row_index, col_index))

        while flash_queue:
            row_index, col_index = flash_queue.popleft()

            # Check to see if indices are inside the matrix
            if row_index < 0 or row_index >= len(matrix) or col_index < 0 or col_index >= len(matrix[row_index]):
                continue

            if matrix[row_index][col_index] == 9:
                step_flashes += 1
                matrix[row_index][col_index] = 0
                neighbors = [(row_index + direction_tuple[0], col_index + direction_tuple[1]) for direction_tuple
                             in directions]
                flash_queue.extend(neighbors)

            elif matrix[row_index][col_index] != 0:
                matrix[row_index][col_index] += 1

        if step_flashes == 100 and part == 2:
            return step + 1

        total_flashes += step_flashes
    return total_flashes


def day_11(part: int = 1):
    with open('../input.txt', 'r') as input_file:
        matrix = [[int(el) for el in line.strip()] for line in input_file.readlines()]

    steps = 100 if part == 1 else 10000
    return day_11_calculate(matrix, steps, part)


if __name__ == '__main__':
    print(day_11(part=1))
    print(day_11(part=2))
