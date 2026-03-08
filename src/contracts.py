from abc import ABC, abstractmethod
import time

class Maze(ABC):

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

    @abstractmethod
    def generate_maze(self) -> Maze:
        pass

    @abstractmethod
    def generate_start_and_goal(self,maze : Maze) -> tuple:
        pass

class Solver:

    @abstractmethod
    def solve(self, maze : Maze, start, goal) -> list:
        pass
