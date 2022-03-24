import math


class Vertex:
    def __init__(self, key):
        self.key = key
        self.distance = math.inf
        self.parent = None

    def __lt__(self, other):
        return self.distance < other.distance

    def __gt__(self, other):
        return self.distance > other.distance

    def __str__(self) -> str:
        parent = self.parent

        if parent:
            parent = parent.key

        return str({"key": self.key, "parent": parent, "d": self.distance})


class Edge:
    def __init__(self, source: Vertex, target: Vertex, distance: int):
        self.source = source
        self.target = target
        self.distance = distance
