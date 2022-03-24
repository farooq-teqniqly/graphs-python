import sys
from heapq import heappush, heappop
from typing import List

from graph_primitives import Vertex, Edge


class Dijkstra:
    def __init__(self, verticies: List[Vertex], edges: List[Edge]):
        self.verticies = verticies
        self.edges = edges

    def compute_paths(self, source: Vertex):
        source.distance = 0
        heap = []
        heappush(heap, source)

        while heap:
            actual_vertex = heappop(heap)

            for edge in [edge for edge in self.edges if edge.source == actual_vertex]:
                v = edge.target
                d = actual_vertex.distance + edge.distance

                if d < v.distance:
                    v.distance = d
                    v.parent = actual_vertex
                    heappush(heap, v)

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

    edges = [
        Edge(v_a, v_b, 4),
        Edge(v_a, v_c, 2),
        Edge(v_b, v_d, 2),
        Edge(v_b, v_c, 3),
        Edge(v_b, v_e, 3),
        Edge(v_c, v_b, 1),
        Edge(v_c, v_e, 5),
        Edge(v_c, v_d, 4),
        Edge(v_e, v_d, 1)
    ]

    d = Dijkstra([v_a, v_b, v_c, v_d, v_e], edges)

    source = v_a
    d.compute_paths(source)

    target = v_e

    sp = d.get_shortest_path(target)

    print([str(v) for v in sp])


if __name__ == "__main__":
    sys.exit(main())
