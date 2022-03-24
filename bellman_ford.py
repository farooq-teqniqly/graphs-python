import sys
from typing import List

from graph_primitives import Vertex, Edge


class BellmanFord:
    def __init__(self, verticies: List[Vertex], edges: List[Edge]):
        self.verticies = verticies
        self.edges = edges

    def compute_paths(self, source: Vertex):
        source.distance = 0

        for i in range(len(self.verticies)):
            for edge in self.edges:
                self.update(edge)

    def update(self, edge: Edge):
        u = edge.source
        v = edge.target

        if u.distance + edge.distance < v.distance:
            v.parent = u

        v.distance = min(v.distance, u.distance + edge.distance)

    def get_shortest_path(self, target: Vertex) -> List[Vertex]:
        path = [target]
        v = target.parent

        while v:
            path.append(v)
            v = v.parent

        path.reverse()

        return path


def main():
    v_a = Vertex("A")
    v_b = Vertex("B")
    v_c = Vertex("C")
    v_d = Vertex("D")
    v_e = Vertex("E")
    v_s = Vertex("S")

    edges = [
        Edge(v_a, v_c, 2),
        Edge(v_b, v_a, 1),
        Edge(v_c, v_b, -2),
        Edge(v_d, v_c, -1),
        Edge(v_d, v_a, -4),
        Edge(v_e, v_d, 1),
        Edge(v_s, v_e, 8),
        Edge(v_s, v_a, 10)
    ]

    bf = BellmanFord([v_a, v_b, v_c, v_d, v_e, v_s], edges)

    source = v_s
    bf.compute_paths(source)

    target = v_b
    sp = bf.get_shortest_path(target)

    print([str(v) for v in sp])


if __name__ == "__main__":
    sys.exit(main())
