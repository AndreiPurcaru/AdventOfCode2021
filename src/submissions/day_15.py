from collections import defaultdict
from queue import PriorityQueue
from typing import Tuple, DefaultDict, List, Dict

import numpy as np

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# TODO clean everything up
def part_2():
    with open('../input.txt', 'r') as input_file:
        initial_matrix = np.array([[int(el) for el in line.strip()] for line in input_file.readlines()])

    new_matrix_part = initial_matrix.copy()
    downwards_extended_matrix = initial_matrix.copy()
    for i in range(4):
        new_matrix_part = (new_matrix_part + 1) % 10
        new_matrix_part = np.where(new_matrix_part == 0, 1, new_matrix_part)
        downwards_extended_matrix = np.append(downwards_extended_matrix, new_matrix_part, 0)

    new_matrix_part = downwards_extended_matrix.copy()
    final_matrix = downwards_extended_matrix.copy()
    for i in range(4):
        new_matrix_part = (new_matrix_part + 1) % 10
        new_matrix_part = np.where(new_matrix_part == 0, 1, new_matrix_part)
        final_matrix = np.append(final_matrix, new_matrix_part, 1)

    print(day_15_graph(final_matrix))


def day_15_parse():
    with open('../input.txt', 'r') as input_file:
        matrix = [[int(el) for el in line.strip()] for line in input_file.readlines()]
    return matrix


def find_lowest_risk_path(matrix):
    n = len(matrix)
    m = len(matrix[0])
    memory = [[n * m * 9 + 1 for _ in range(m)] for _ in range(n)]
    memory[0][0] = 0

    for k in range(10):
        for row_index, row in enumerate(matrix):
            for col_index, el in enumerate(row):
                if row_index == 0 and col_index == 0:
                    continue
                # TODO: change to use directions list
                memory[row_index][col_index] = min(memory[row_index - 1][col_index] + el, memory[row_index][col_index]) if row_index - 1 >= 0 else memory[row_index][col_index]
                memory[row_index][col_index] = min(memory[row_index][col_index - 1] + el, memory[row_index][col_index]) if col_index - 1 >= 0 else memory[row_index][col_index]
                memory[row_index][col_index] = min(memory[row_index + 1][col_index] + el, memory[row_index][col_index]) if row_index + 1 < n else memory[row_index][col_index]
                memory[row_index][col_index] = min(memory[row_index][col_index + 1] + el, memory[row_index][col_index]) if col_index + 1 < m else memory[row_index][col_index]

    return memory[n - 1][m - 1]


def day_15_graph(matrix):
    matrix_dict: DefaultDict[Tuple[int, int], int] = defaultdict(int)

    for row_index, line in enumerate(matrix):
        for col_index, el in enumerate(line):
            matrix_dict[(row_index, col_index)] = int(el)

    n, m = 0, 0
    for pair in matrix_dict:
        n = max(n, pair[0])
        m = max(m, pair[1])

    n += 1
    m += 1

    nodes: DefaultDict[str, Dict[str, int]] = defaultdict(dict)

    for coord, weight in matrix_dict.copy().items():
        node_id = f"{coord[0]}_{coord[1]}"

        for direction in DIRECTIONS:
            neighbour_coord = (coord[0] + direction[0], coord[1] + direction[1])
            neighbour_weight = matrix_dict[neighbour_coord]

            if neighbour_weight == 0:
                continue

            neighbour_id = f"{neighbour_coord[0]}_{neighbour_coord[1]}"
            nodes[node_id].update({neighbour_id: neighbour_weight})

    visited: DefaultDict[str, bool] = defaultdict(bool)
    distance: DefaultDict[str, int] = defaultdict(lambda: n * m * 9 + 1)

    start_node_id = "0_0"
    distance[start_node_id] = 0
    end_node_id = f"{n - 1}_{m - 1}"

    queue = PriorityQueue()
    queue.put((0, start_node_id))

    while queue:
        current_id: str = queue.get()[1]
        visited[current_id] = True
        if current_id == end_node_id:
            return distance[current_id]
        for to, weight in nodes[current_id].items():
            new_distance = distance[current_id] + weight
            if not visited[to] and new_distance < distance[to]:
                queue.put((new_distance, to))
                distance[to] = new_distance


if __name__ == '__main__':

    # print(find_lowest_risk_path(day_15_parse()))
    print(part_2())
    # print(day_15_graph(parse))
