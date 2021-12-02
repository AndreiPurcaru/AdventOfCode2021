from typing import List


def day_2_1(lines: List[str]):
    horizontal_pos = 0
    depth_pos = 0
    for line in lines:
        command, amount = line.split()
        amount = int(amount)
        match command:
            case 'forward':
                horizontal_pos += amount
            case 'down':
                depth_pos += amount
            case 'up':
                depth_pos -= amount

    return horizontal_pos * depth_pos


def day_2_2(lines: List[str]):
    horizontal_pos = 0
    depth_pos = 0
    aim = 0
    for line in lines:
        command, amount = line.split()
        amount = int(amount)
        match command:
            case 'forward':
                horizontal_pos += amount
                depth_pos += aim * amount
            case 'down':
                aim += amount
            case 'up':
                aim -= amount

    return horizontal_pos * depth_pos

def day_2(part=1):
    with open('../input.txt', 'r') as input_file:
        input_values = input_file.readlines()

    return day_2_1(input_values) if part == 1 else day_2_2(input_values)


if __name__ == '__main__':
    print(day_2(part=1))
    print(day_2(part=2))