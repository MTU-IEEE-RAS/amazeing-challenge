from ..contracts import Generator, Maze
from ..mazes.dummy_maze import DummyMaze

class DummyGenerator(Generator):

    def generate_maze(self, seed=None) -> Maze:
        """Generates a dummy maze.

        Args:
            seed: an unused seed.

        Returns:
            A dummy maze.
        """
        return DummyMaze()
    
    def generate_start_and_goal(self, maze):
        """Generates a dummy start and goal point.

        Args:
            maze: A maze.

        Returns:
            A tuple of nones.
        """
        return (None,None)