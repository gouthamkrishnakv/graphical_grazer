from typing import Dict, Optional

from graphical_grazer.node import Node


class Graph:
    graph: Dict[int, Node]

    def __init__(self) -> None:
        self.graph = {}

    def clear_nodes(self):
        for i in self.graph.values():
            i.visited = False
            i.next_ele = None

    def visit(self, ele: int):
        if ele not in self.graph:
            self.graph[ele] = Node(ele)
        if self.graph[ele].visited:
            return ele
        self.graph[ele].visited = True
        nele = None
        if ele % 2 == 0:
            nele = int(ele / 2)
        else:
            nele = int(3 * ele + 1)
        self.visit(nele)
        self.graph[ele].next_ele = self.graph[nele]
        return ele
