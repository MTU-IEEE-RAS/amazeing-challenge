from abc import ABC, abstractmethod
import time

class Maze(ABC):
    """Abstract Class for Maze
    """

    @abstractmethod
    def add_edge(self,n1,n2):
        pass

    @abstractmethod
    def remove_edge(self,n1,n2):
        pass

    @abstractmethod
    def has_edge(self,n1,n2) -> bool:
        pass

    @abstractmethod
    def get_edges(self,n) -> list:
        pass

class Generator(ABC):
    """Abstract class for Maze Generators
    """

    @abstractmethod
    def generate_maze(self) -> Maze:
        pass

    @abstractmethod
    def generate_start_and_goal(self,maze : Maze) -> tuple:
        pass

class Solver:
    """Abstract class for Solvers
    """

    @abstractmethod
    def solve(self, maze : Maze, start, goal) -> list:
        pass
