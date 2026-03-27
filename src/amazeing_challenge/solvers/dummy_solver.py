from ..contracts import Solver, Maze
from typing import Iterator, List

class DummySolver(Solver):

    def solve(self, maze : Maze, start, goal) -> Iterator[List]:
        yield []