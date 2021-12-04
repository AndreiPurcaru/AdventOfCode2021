from typing import Dict, List

import numpy as np


def day_4_calculate(bingo_numbers: List[int], bingo_boards: List[List[List[int]]],
                    bingo_boards_numbers: Dict[int, List[tuple[int, int, int]]], part: int = 1):
    used = set()
    last_board: List[List[int]] = []
    last_bingo_number: int = 0
    for bingo_number_index, bingo_number in enumerate(bingo_numbers):
        if len(used) == len(bingo_boards):
            break
        if bingo_number in bingo_boards_numbers:
            coords = bingo_boards_numbers.get(bingo_number)
            for bingo_board_index, row_index, el_index in coords:
                if bingo_board_index in used:
                    continue
                bingo_boards[bingo_board_index][row_index][el_index] = 0
                row_sum = sum(bingo_boards[bingo_board_index][row_index])
                col_sum = sum([bingo_boards[bingo_board_index][i][el_index] for i in range(5)])
                if row_sum == 0 or col_sum == 0:
                    used.add(bingo_board_index)
                    if part == 1:
                        return np.sum(bingo_boards[bingo_board_index]) * bingo_number
                    else:
                        last_board = bingo_boards[bingo_board_index].copy()
                        last_bingo_number = bingo_number
    return np.sum(last_board) * last_bingo_number


def day_4(part: int = 1):
    with open('../input.txt', 'r') as input_file:
        bingo_numbers = list(map(int, input_file.readline().strip().split(',')))
        bingo_boards_list = [list(map(int, line.strip().split())) for line in input_file.readlines() if
                             line.strip() != '']

    bingo_boards: List[List[List[int]]] = [bingo_boards_list[i:i + 5] for i in range(0, len(bingo_boards_list), 5)]

    bingo_boards_numbers: Dict[int, List[tuple[int, int, int]]] = {}

    for bingo_board_index, bingo_board in enumerate(bingo_boards):
        for row_index, row in enumerate(bingo_board):
            for el_index, el in enumerate(row):
                bingo_boards_numbers.setdefault(int(el), []).append((bingo_board_index, row_index, el_index))

    return day_4_calculate(bingo_numbers, bingo_boards, bingo_boards_numbers, part)


if __name__ == '__main__':
    print(day_4(part=1))
    print(day_4(part=2))
