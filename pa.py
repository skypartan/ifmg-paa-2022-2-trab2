from __future__ import annotations
import random
from typing import Generator


class Node:

    def __init__(self, value: int | None = None) -> None:
        self.left: Node | None = None
        self.right: Node | None = None
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class ABP:
    
    def __init__(self) -> None:
        self.root = Node()
    
    def add(self, value: int) -> ABP:
        if self.root is None or self.root.value is None:
            self.root = Node(value)
            return self

        node = self.root
        while True:
            if node.value > value: # left
                node = self.root.left
                if node is None:
                    node = Node(value) 
                    break
            
            else: # right
                node = self.root.right
                if node is None:
                    node = Node(value) 
                    break

        return self

    def remove(self, value: int) -> ABP:

        return self

    def search(self, value: int) -> Node | None:
        nodes = self._inorder_list(self.root)
    
    def height(self) -> int:
        return 0

    def inorder(self) -> list[Node]:
        data = self._inorder_list(self.root)
        return data

    def _inorder_list(self, start: Node | None) -> list[Node]:
        nodes: list[Node] = []

        if start is not None:
            nodes = self._inorder_list(start.left)
            nodes.append(start)
            nodes += self._inorder_list(start.right)

        return nodes

    def _inorder_search(self, start: Node | None, value: int) -> Generator:
        if start is not None:
            yield from self._inorder_list(start.left)
            if start.value == value:
                yield start
            yield from self._inorder_list(start.right)



if __name__ == "__main__":
    tree = ABP()

    for i in range(100):
        tree.add(random.randint(0, 1000))
    
    print("tree =", tree.inorder())
    print("tree height =", tree.height())
