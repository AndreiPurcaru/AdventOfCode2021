from collections import defaultdict
from typing import DefaultDict, List


class Graph:
    def __repr__(self):
        return f"Graph(graph={self.edges})"

    def __init__(self):

        # Use default dictionary to give each node an empty list of neighbors
        self.edges: DefaultDict[str, List[str]] = defaultdict(list)

    def add_edge(self, from_node: str, to_node: str):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)

    def add_edges_from_tuple_list(self, tuple_list: List[List[str]]):
        for pair in tuple_list:
            self.add_edge(pair[0], pair[1])

    def _find_all_paths_count_rec(self, visited: DefaultDict[str, bool], current: str = 'start', end: str = 'end',
                                  can_visit_twice: str = '', part: int = 1):

        count = 0

        if current.islower() and current != end:
            visited[current] = True

        if current == end:
            return 1
        else:
            for node in self.edges[current]:
                if not visited[node]:
                    count += self._find_all_paths_count_rec(visited, current=node, can_visit_twice=can_visit_twice,
                                                            part=part)
                elif not can_visit_twice and node != 'start' and part == 2:
                    count += self._find_all_paths_count_rec(visited, current=node, can_visit_twice=node, part=part)

        if current != 'start' and current != can_visit_twice:
            visited[current] = False
        return count

    def find_all_paths_count(self, part: int = 1):
        visited = defaultdict(lambda: False)
        return self._find_all_paths_count_rec(visited, part=part)


def day_12(part: int = 1):
    with open('../input.txt', 'r') as input_file:
        edges: List[List[str]] = [line.strip().split('-') for line in input_file.readlines()]

    graph = Graph()
    graph.add_edges_from_tuple_list(edges)

    return graph.find_all_paths_count(part)


if __name__ == '__main__':
    print(day_12(part=1))
    print(day_12(part=2))
