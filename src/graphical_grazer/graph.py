from typing import Dict

from graphical_grazer.node import Node


class Graph:
    vertices: Dict[int, Node]

    def __init__(self) -> None:
        self.vertices = {}

    def clear_nodes(self):
        for i in self.vertices.values():
            i.visited = False
            i.next_ele = None

    def visit(self, ele: int):
        if ele not in self.vertices:
            self.vertices[ele] = Node(ele)
        if self.vertices[ele].visited:
            return ele
        self.vertices[ele].visited = True
        nele = None
        if ele % 2 == 0:
            nele = int(ele / 2)
        else:
            nele = int(3 * ele + 1)
        self.visit(nele)
        self.vertices[ele].next_ele = self.vertices[nele]
        return ele
