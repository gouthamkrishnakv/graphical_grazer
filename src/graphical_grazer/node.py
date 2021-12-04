from typing import Optional


class Node:
    ele: int
    next_ele: Optional["Node"]
    visited: bool

    def __init__(self, ele: int, next: Optional["Node"] = None) -> None:
        self.ele = ele
        self.next_ele = next
        self.visited = False

    def __hash__(self) -> int:
        return hash(self.ele)

    def __eq__(self, __o: object) -> bool:
        if type(self) == type(__o):
            __o: "Node"
            return self.ele == __o.ele
        return False

    def __ne__(self, __o: object) -> bool:
        if type(self) != type(__o):
            return True
        __o: "Node"
        return self.ele != __o.ele

    def __repr__(self) -> str:
        if self.next_ele is not None:
            return f"<({self.ele}, {self.next_ele.ele})>"
        else:
            return f"<{self.ele}>"
