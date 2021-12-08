from typing import List, Dict

def find_digits_with_six_segments(length_to_segments_dict: Dict[int, List[frozenset[str]]], known_digits_dict: Dict[int, frozenset[str]]):
    digits_that_use_six_segments = length_to_segments_dict[6]
    one = known_digits_dict[1]
    four = known_digits_dict[4]
    for el in digits_that_use_six_segments:
        if len(el - one) == 5:
            known_digits_dict[6] = el
        elif len(el - four) == 2:
            known_digits_dict[9] = el
    digits_that_use_six_segments.remove(known_digits_dict[6])
    digits_that_use_six_segments.remove(known_digits_dict[9])
    known_digits_dict[0] = digits_that_use_six_segments[0]


def find_digits_with_five_segments(length_to_segments_dict: Dict[int, List[frozenset[str]]], known_digits_dict: Dict[int, frozenset[str]]):
    digits_that_use_five_segments = length_to_segments_dict[5]
    one = known_digits_dict[1]
    nine = known_digits_dict[9]
    for el in digits_that_use_five_segments:
        if len(el - one) == 3:
            known_digits_dict[3] = el
        elif len(nine - el) == 1:
            known_digits_dict[5] = el

    digits_that_use_five_segments.remove(known_digits_dict[3])
    digits_that_use_five_segments.remove(known_digits_dict[5])
    known_digits_dict[2] = digits_that_use_five_segments[0]


def day_8_1(output_values: List[List[str]]):
    sure_digits = [list(filter(lambda length: (length in (2, 3, 4, 7)), [len(element) for element in elements])) for elements in output_values]
    count = sum(map(len, sure_digits))
    return count


def day_8_2(input_values: List[List[str]], output_values: List[List[str]]):

    counter = 0

    for index, line in enumerate(input_values):
        length_to_segments_dict: Dict[int, List[frozenset[str]]] = {}
        known_digits_dict: Dict[int, frozenset[str]] = {}

        for element in line:
            length = len(element)
            length_to_segments_dict.setdefault(length, []).append(frozenset(element))

        known_digits_dict[1] = length_to_segments_dict.get(2)[0] # We know for sure there is only one el with 2 segments used and that el is 1
        known_digits_dict[4] = length_to_segments_dict.get(4)[0] # We know for sure there is only one el with 4 segments used and that el is 4
        known_digits_dict[7] = length_to_segments_dict.get(3)[0] # We know for sure there is only one el with 3 segments used and that el is 7
        known_digits_dict[8] = length_to_segments_dict.get(7)[0] # We know for sure there is only one el with 7 segments used and that el is 8

        find_digits_with_six_segments(length_to_segments_dict, known_digits_dict)
        find_digits_with_five_segments(length_to_segments_dict, known_digits_dict)

        set_to_value_dict: Dict[frozenset[str], int] = {value: key for key, value in known_digits_dict.items()}

        number = 0
        p = 10

        for output in output_values[index]:
            number = number * p + set_to_value_dict[frozenset(output)]
        counter += number

    return counter


def day_8(part: int = 1):
    with open('../input.txt', 'r') as input_file:
        lines = [[el.strip().split() for el in line.split('|')] for line in input_file.readlines()]

    input_values = [line[0] for line in lines]
    output_values = [line[1] for line in lines]

    return day_8_1(output_values) if part == 1 else day_8_2(input_values, output_values)


if __name__ == '__main__':
    print(day_8(part=1))
    print(day_8(part=2))