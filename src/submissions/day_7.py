from math import floor
from statistics import median, mean
from typing import List

def gauss_sum(n: int):
    return n * (n+1) // 2


def day_7_1(positions: List[int]):
    median_value = median(positions)

    fuel_consumption_list = list(map(lambda element: abs(element - median_value), positions))
    fuel_consumption = sum(fuel_consumption_list)

    return int(fuel_consumption)


def day_7_2(positions: List[int]):
    mean_value = int(floor(mean(positions)))

    fuel_consumption_list = list(map(lambda element: gauss_sum(abs(element - mean_value)), positions))
    fuel_consumption = sum(fuel_consumption_list)


    return fuel_consumption

def day_7(part: int = 1):
    with open('../input.txt') as input_file:
        positions = [int(number) for number in input_file.readline().split(',')]

    return day_7_1(positions) if part == 1 else day_7_2(positions)


if __name__ == '__main__':
    print(day_7(part=1))
    print(day_7(part=2))