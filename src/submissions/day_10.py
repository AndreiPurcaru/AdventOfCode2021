from typing import List, Dict


def day_10_1(lines: List[str], matching_pairs: Dict[str, str]):
    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    total = 0
    for line in lines:
        parenthesis_stack = []
        for el in line:
            if el in matching_pairs.values():
                parenthesis_stack.append(el)
            elif parenthesis_stack:
                last_parenthesis = parenthesis_stack.pop()
                if matching_pairs[el] != last_parenthesis:
                    total += points[el]
                    break
    return total


def day_10_2(lines: List[str], matching_pairs: Dict[str, str]):
    points = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4
    }

    totals = []
    for line in lines:
        parenthesis_stack = []
        corrupted = False
        for el in line:
            if el in matching_pairs.values():
                parenthesis_stack.append(el)
            elif parenthesis_stack:
                last_parenthesis = parenthesis_stack.pop()
                if matching_pairs[el] != last_parenthesis:
                    corrupted = True
                    break
        if not corrupted:
            total = 0
            for not_closed in reversed(parenthesis_stack):
                total = total * 5 + points[not_closed]
            totals.append(total)
    totals.sort()
    return totals[len(totals) // 2]


def day_10(part: int = 1):
    with open('../input.txt', 'r') as input_file:
        lines = [line.strip() for line in input_file.readlines()]

    matching_pairs = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<'
    }

    return day_10_1(lines, matching_pairs) if part == 1 else day_10_2(lines, matching_pairs)


if __name__ == '__main__':
    print(day_10(part=1))
    print(day_10(part=2))