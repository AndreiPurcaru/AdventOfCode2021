from dataclasses import dataclass
from typing import List


@dataclass(slots=True, frozen=True)
class Point:
    x: int
    y: int

@dataclass(slots=True, frozen=True)
class Line:
    p1: Point
    p2: Point

def day_5_calculate(lines: List[Line], diagram: List[List[int]], part: int = 1):
    danger = 0

    for line in lines:
        start_x, end_x = line.p1.x, line.p2.x
        start_y, end_y = line.p1.y, line.p2.y

        if line.p1.x == line.p2.x or line.p1.y == line.p2.y:

            if line.p1.x > line.p2.x:
                start_x, end_x = line.p2.x, line.p1.x
            if line.p1.y > line.p2.y:
                start_y, end_y = line.p2.y, line.p1.y

            for i in range(start_y, end_y + 1):
                for j in range(start_x, end_x + 1):
                    diagram[i][j] += 1
                    if diagram[i][j] == 2:
                        danger += 1
        # We are dealing with diagonals
        elif part == 2:

            step_x = 1 if start_x < end_x else -1
            step_y = 1 if start_y < end_y else -1

            diagonal_list = list(zip(range(start_y, end_y + step_y, step_y), range(start_x, end_x + step_x, step_x)))
            for i, j in diagonal_list:
                diagram[i][j] += 1
                if diagram[i][j] == 2:
                    danger += 1

    return danger


def day_5(part: int = 1):

    with open('../input.txt', 'r') as input_file:
        points_list = [line.strip().split(' -> ') for line in input_file.readlines()]

    points_list_clean = [(lambda points: (points[0].split(','), points[1].split(',')))(line) for line in points_list]
    lines = [Line(Point(int(points[0][0]), int(points[0][1])), Point(int(points[1][0]), int(points[1][1]))) for points in points_list_clean]

    max_x = 0
    max_y = 0

    for line in lines:
        max_x = max(max_x, line.p1.x, line.p2.x)
        max_y = max(max_y, line.p1.y, line.p2.y)

    diagram = [[0 for col in range(max_x + 1)] for row in range(max_y + 1)]

    return day_5_calculate(lines, diagram, part)

if __name__ == '__main__':
    print(day_5(part=1))
    print(day_5(part=2))