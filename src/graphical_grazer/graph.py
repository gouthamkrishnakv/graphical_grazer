from typing import Dict, Optional

from graphical_grazer.node import Node


class Graph:
    vertices: Dict[int, Node]

    def __init__(self) -> None:
        self.vertices = {}

    def clear_nodes(self):
        # For all vertices
        for i in self.vertices.values():
            # Clear the "next element" variable and the visited flag.
            i.visited = False
            i.next_ele = None

    def visit(self, ele: int):
        """
        `visit` Method

        This contains the special case where the elements were already created but 
        cleared of visiting.
        
        This is useful in cases where one needs to iterate through
        the graph again without regenerating the entire graph.
        """
        # "element is not created" situation
        if ele not in self.vertices:
            # Create the element
            self.vertices[ele] = Node(ele)
        # If element is not visited
        if not self.vertices[ele].visited:
            # Update the current element to visited
            self.vertices[ele].visited = True
            # Initialize next element to none
            nele: Optional[int] = None
            # If current element is even
            if ele % 2 == 0:
                # Take half
                nele = int(ele / 2)
            # If the current element is odd
            else:
                # Else thrice the element and add 1
                nele = int(3 * ele + 1)
            # Visit the next element
            self.visit(nele)
            # Join the "next" for current to the next element
            self.vertices[ele].next_ele = self.vertices[nele]
