from collections import deque
from typing import List

class FishCounter:
    __slots__ = ('deque',)

    def __init__(self, fish_times: List[int]):
        counter = [fish_times.count(reproduce_time) for reproduce_time in range(9)]
        self.deque = deque(counter)


def day_6(days: int):
    with open('../input.txt', 'r') as input_file:
        fish_times = list(map(int, input_file.readline().split(',')))

    fish_counter = FishCounter(fish_times)
    for _ in range(days):
        current_reproducing_fish = fish_counter.deque.popleft()
        fish_counter.deque.append(0)
        fish_counter.deque[6] += current_reproducing_fish
        fish_counter.deque[8] += current_reproducing_fish

    return sum(fish_counter.deque)


if __name__ == '__main__':
    print(day_6(days=80))
    print(day_6(days=256))