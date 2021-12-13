from typing import List

import numpy as np
import pandas as pd
from numpy.typing import NDArray


def convert_to_readable_format(matrix: NDArray[bool]):
    return np.where(matrix == True, '#', '.')


# Assumed the fold will always result in a smaller bottom/left side
def day_13_calculate(matrix: NDArray[bool], folds: List[List[str]]):
    for fold in folds:
        if fold[0] == 'x':
            x = int(fold[1])
            left_fold: NDArray[bool] = matrix[:, :x]
            right_fold: NDArray[bool] = matrix[:, x + 1:]
            flipped_right_fold: NDArray[bool] = np.fliplr(right_fold)

            # Pad left to ensure sizes match
            flipped_right_fold = np.pad(flipped_right_fold,
                                        ((0, 0), (left_fold.shape[1] - flipped_right_fold.shape[1], 0)),
                                        constant_values=False)

            matrix = np.logical_or(left_fold, flipped_right_fold)
        else:
            y = int(fold[1])
            top_fold: NDArray[bool] = matrix[:y, :]
            bottom_fold: NDArray[bool] = matrix[y + 1:, :]
            flipped_bottom_fold: NDArray[bool] = np.flipud(bottom_fold)

            # Pad top to ensure sizes match
            flipped_bottom_fold = np.pad(flipped_bottom_fold,
                                         ((top_fold.shape[0] - flipped_bottom_fold.shape[0], 0), (0, 0)),
                                         constant_values=False)

            matrix = np.logical_or(top_fold, flipped_bottom_fold)

    return matrix


def day_13(part: int = 1):
    folds = []
    coords = []

    with open('../input.txt', 'r') as input_file:
        for line in input_file:
            if 'fold' in line:
                folds.append(line.strip().split()[-1].split('='))
            elif ',' in line:
                coords.append(tuple(map(int, line.strip().split(','))))

    max_x, max_y = 0, 0

    for el in coords:
        max_x = max(max_x, el[0])
        max_y = max(max_y, el[1])

    matrix = np.full((max_y + 1, max_x + 1), False)

    for el in coords:
        matrix[el[1], el[0]] = True

    if part == 1:
        return np.count_nonzero(day_13_calculate(matrix, folds[:1]))
    else:
        response = convert_to_readable_format(day_13_calculate(matrix, folds))
        pd.set_option("display.max_rows", None, "display.max_columns", None)
        dataframe = pd.DataFrame(response)
        return dataframe


if __name__ == '__main__':
    print(day_13(part=1))
    print(day_13(part=2))
