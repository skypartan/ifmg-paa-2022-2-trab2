from __future__ import annotations
import random
from turtle import right
from typing import Generator


class Node:

    def __init__(self, value: int) -> None:
        self.left: Node | None = None
        self.right: Node | None = None
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


class ABP:

    def __init__(self) -> None: 
        self.root: Node | None = None

    def add(self, value: int) -> ABP:
        if self.root is None:
            self.root = Node(value)
            return self

        node: Node = self.root
        while True:
            if node.value > value: # left
                if node.left is None:
                    node.left = Node(value) 
                    break
                else:
                    node = node.left

            else: # right
                if node.right is None:
                    node.right = Node(value) 
                    break
                else:
                    node = node.right

        return self

    def height(self) -> int:
        return self._height(self.root)

    def _height(self, start: Node | None) -> int:
        if start is None:
            return 0

        lheight = self._height(start.left)
        rheight = self._height(start.right)

        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1

    def inorder(self) -> list[Node]:
        return self._inorder(self.root)

    def _inorder(self, start: Node | None) -> list[Node]:
        nodes: list[Node] = []

        if start is not None:
            nodes = self._inorder(start.left)
            nodes.append(start)
            nodes += self._inorder(start.right)

        return nodes
    
    def paths(self) -> list[list[Node]]:
        return self._paths(self.root)

    def _paths(self, start: Node | None) -> list[list[Node]]:
        if start is None:
            return []
        
        paths = self._paths(start.left)
        paths += self._paths(start.right)

        if paths == []:
            return [[start]]

        for i in paths:
            i.append(start)

        return paths


if __name__ == "__main__":
    tree = ABP()

    for i in range(10):
        tree.add(random.randint(0, 1000))

    if tree.root is not None:
        tree.root.display()

    print("tree = [", end="")
    for node in tree.inorder():
        print(node.value, ",", end="")
    print("]")

    print("tree height =", tree.height())

    print("paths = [")
    paths = tree.paths()
    for path in paths:
        print("path = [", end="")
        for node in path:
            print(node.value, ",", end="")
        print("]")
    print("\t]")
