from abc import ABC, abstractmethod
import time
from typing import Iterator, List

class Maze(ABC):
    """Abstract Class for Maze
    """

    @abstractmethod
    def add_edge(self,n1,n2):
        """Add an edge between node 1 and node 2 if possible and not already connected.
        """
        pass

    @abstractmethod
    def remove_edge(self,n1,n2):
        """Remove the edge between node 1 and node 2 if connected.
        """
        pass

    @abstractmethod
    def has_edge(self,n1,n2) -> bool:
        """Check for an edge between node 1 and node 2.
        """
        pass

    @abstractmethod
    def get_edges(self,n) -> list:
        """Get all edges node 'n' has.
        """
        pass
    
class Generator(ABC):
    """Abstract class for Maze Generators
    """

    @abstractmethod
    def generate_maze(self, seed=None) -> Maze:
        """Generate a random maze using a seed if one is given.
        """
        pass

    @abstractmethod
    def generate_start_and_goal(self,maze : Maze, seed=None) -> tuple:
        """Generate a random start and goal point using a seed if one is given.
        """
        pass

class Solver:
    """Abstract class for Solvers
    """

    @abstractmethod
    def solve(self, maze : Maze, start, goal) -> Iterator[List]:
        """Give a maze, a start, and an goal point, create a valid path to the start and end.
        """
        pass
