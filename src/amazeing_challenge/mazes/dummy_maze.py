from ..contracts import Maze

class DummyMaze(Maze):
    """An example maze implementation.
    """

    def add_edge(self,n1, n2):
        """Does nothing.
        """
        pass

    def remove_edge(self,n1, n2):
        """Does nothing.
        """
        pass

    def has_edge(self,n1, n2):
        """Does nothing.
        """
        pass

    def get_edges(self,n):
        """Does nothing.
        """
        pass