from collections import deque


class Node:

    def __init__(self, val):
        self.val = val
        self.in_deg = 0

    def __hash__(self):
        return hash(self.val)

    def __repr__(self):
        return str(self.val)

class Graph:

    def __init__(self, init={}, directed=False):
        self.vertices = {}
        self.directed = directed
        for k, v in init.items():
            for node in v:
                self.add_edge(k, node)

    def add_node(self, val):
        if val not in self.vertices:
            self.vertices[val] = []

    def add_edge(self, source, target):
        if not source in self.vertices or not target in self.vertices:
            self.add_node(source)
            self.add_node(target)

        self.vertices[source].append(target)
        target.in_deg += 1

        if not self.directed:
            self.add_node(target)
            self.vertices[target].append(source)
            source.in_deg += 1

    def bfs(self, source, sorted_list):
        visited = {source}
        queue = deque([source])

        while queue:
            curr = queue.popleft()
            sorted_list.append(curr)
            for neighbor in self.vertices[curr]:
                if neighbor not in visited:
                    neighbor.in_deg -= 1
                    if neighbor.in_deg == 0:
                        visited.add(neighbor)
                        queue.append(neighbor)

    def top_sort(self):
        sorted_list = []
        start = []

        for node in self.vertices:
            if node.in_deg == 0:
                start.append(node)

        for node in start:
            self.bfs(node, sorted_list)

        if len(sorted_list) != len(self.vertices):
            raise Exception('sorting is not possible')

        return sorted_list

    def print(self):
        for v in self.vertices:
            print(f'{v}:', end=' ')
            for neighbor in self.vertices[v]:
                print(neighbor, end=' ')
            print('\n')


def main():
    one, two, three, four = Node(1), Node(2), Node(3), Node(4)
    five, six, seven, eight = Node(5), Node(6), Node(7), Node(8)
    g = Graph({one: [two, three, four],
               two: [five, three],
               three: [five],
               four: [three, five],
               six: [seven, eight]}, True)
    print(g.top_sort())


if __name__ == '__main__':
    main()
