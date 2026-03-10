from ..contracts import Generator, Maze
from ..mazes.dummy_maze import DummyMaze

class DummyGenerator(Generator):

    def generate_maze(self) -> Maze:
        return DummyMaze()
    
    def generate_start_and_goal(self, maze):
        return (None,None)