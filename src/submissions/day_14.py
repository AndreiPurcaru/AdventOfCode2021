from collections import defaultdict, Counter
from typing import Dict, DefaultDict


def count_kids_rec(current: str, pair_insertions: Dict[str, str], counter_dict: Dict[str, int], step: int = 0) -> None:
    if current not in pair_insertions or step == 10:
        return

    insert = pair_insertions.get(current)
    counter_dict[insert] += 1

    count_kids_rec(f"{current[0]}{insert}", pair_insertions, counter_dict, step + 1)
    count_kids_rec(f"{insert}{current[1]}", pair_insertions, counter_dict, step + 1)


def day_14_2(pair_insertions: Dict[str, str], current_pairs_count: DefaultDict[str, int],
             counter_dict: DefaultDict[str, int], steps: int = 40):
    for step in range(steps):
        new_pairs: DefaultDict[str, int] = defaultdict(int)
        for pair in current_pairs_count:
            if pair not in pair_insertions:
                continue

            insert = pair_insertions.get(pair)
            counter_dict[insert] += current_pairs_count[pair]

            new_pairs[pair[0] + insert] += current_pairs_count[pair]
            new_pairs[insert + pair[1]] += current_pairs_count[pair]
        current_pairs_count = new_pairs


def day_14(part: int = 1):
    with open('../input.txt', 'r') as input_file:
        template: str = input_file.readline().strip()
        input_file.readline()
        pair_insertions: Dict[str, str] = {}
        for line in input_file:
            pair = line.strip().split(' -> ')
            pair_insertions[pair[0]] = pair[1]

    counter_dict: DefaultDict[str, int] = defaultdict(int)
    counter_dict.update(Counter(template))
    current_pairs_count: DefaultDict[str, int] = defaultdict(int)

    for start_index in range(0, len(template) - 1):
        current: str = template[start_index: start_index + 2]
        current_pairs_count[current] += 1
        if part == 1:
            return count_kids_rec(current, pair_insertions, counter_dict)

    day_14_2(pair_insertions, current_pairs_count, counter_dict, 40)

    return max(counter_dict.values()) - min(counter_dict.values())


if __name__ == '__main__':
    print(day_14(part=1))
    print(day_14(part=2))
