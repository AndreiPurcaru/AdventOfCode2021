from typing import Generator, List


def day_1_1(input_values: Generator[int, any, None]):

    result = 0
    prev = next(input_values)

    for current_value in input_values:
        if prev < current_value:
            result += 1
        prev = current_value

    return result

def day_1_2(input_values: List[int]):

    result = 0
    previous_sum = sum(input_values[0:3])

    for index, _ in enumerate(input_values, 2):
        current_sum = sum(input_values[index - 2: index + 1])
        if current_sum > previous_sum:
            result += 1
        previous_sum = current_sum
    return result

def day_1(part=1):
    with open('../input.txt', 'r') as input_file:
        input_values = (int(line) for line in input_file.readlines())

    return day_1_1(input_values) if part == 1 else day_1_2(list(input_values))


if __name__ == '__main__':
    print(day_1(part=1))
    print(day_1(part=2))