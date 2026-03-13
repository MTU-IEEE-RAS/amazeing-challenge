from ..contracts import Maze

class DummyMaze(Maze):

    def add_edge(self,n1, n2):
        pass

    def remove_edge(self,n1, n2):
        pass

    def has_edge(self,n1, n2):
        pass

    def get_edges(self,n):
        pass