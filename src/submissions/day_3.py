import numpy as np
from numpy.typing import NDArray


def day_3_1(binary_matrix: NDArray[int], library_mode=False):
    most_common_list = [
        (lambda occurrences: '0' if len(occurrences) == 1 else ('0' if occurrences[0] > occurrences[1] else '1'))(
            np.bincount(column)) for column in binary_matrix.T]

    string_representation = ''.join(most_common_list)
    max_bin_nr = 2 ** (binary_matrix.shape[1]) - 1
    gamma = int(string_representation, 2)
    epsilon = max_bin_nr - gamma

    return string_representation if library_mode else gamma * epsilon


def day_3_2(binary_matrix: NDArray[int]):
    most_common_el_string_rep = day_3_1(binary_matrix, True)

    binary_matrix_most = np.copy(binary_matrix)
    binary_matrix_least = np.copy(binary_matrix)

    length = len(most_common_el_string_rep)

    result_most = find_element(binary_matrix_most, length, most_common_el_string_rep, most=True)
    result_least = find_element(binary_matrix_least, length, most_common_el_string_rep, most=False)

    return int(result_most, 2) * int(result_least, 2)


def find_element(binary_matrix, length, most_common_el_string_rep, most: bool = True):
    result = None
    for index in range(length):
        most_common_el = most_common_el_string_rep[index]

        if most:
            bool_array = np.array([(lambda r, i: r[i] == int(most_common_el))(row, index) for row in binary_matrix])
        else:
            bool_array = np.array([(lambda r, i: r[i] != int(most_common_el))(row, index) for row in binary_matrix])

        binary_matrix = binary_matrix[bool_array]
        if binary_matrix.shape[0] == 1:
            result = ''.join(map(str, binary_matrix[0].tolist()))
            break
        most_common_el_string_rep = day_3_1(binary_matrix, True)
    return result


def day_3(part=1):
    with open('../input.txt', 'r') as input_file:
        input_values = input_file.readlines()
    binary_matrix_list = []
    for line in input_values:
        line_list = []
        for char in line[:len(line) - 1]:
            line_list.append(int(char))
        binary_matrix_list.append(line_list)

    binary_matrix = np.array(binary_matrix_list)

    return day_3_1(binary_matrix) if part == 1 else day_3_2(binary_matrix)


if __name__ == '__main__':
    print(day_3(part=1))
    print(day_3(part=2))
