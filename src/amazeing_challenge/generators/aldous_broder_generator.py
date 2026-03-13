from ..contracts import Generator, Maze
from ..mazes.adjacency_list_maze import AdjacencyListMaze
import random

class AldousBroderGenerator(Generator):

    def generate_maze(self,seed=None,rows=5,cols=5) -> Maze:

        maze = AdjacencyListMaze(rows,cols)

        unvisited = maze.get_nodes()

        if seed != None:
            random.seed(seed)

        current_node = unvisited[random.randint(0,len(unvisited)-1)]
        unvisited.remove(current_node)

        while len(unvisited) > 0:
            neighbors = maze.get_node_neighbors(current_node)

            neighbor = neighbors[random.randint(0,len(neighbors)-1)]

            if neighbor in unvisited:
                maze.add_edge(current_node,neighbor)
                unvisited.remove(neighbor)

            current_node = neighbor

        return maze
        

    def generate_start_and_goal(self,maze : Maze) -> tuple:
        start = (random.randint(0,maze.get_rows()-1), random.randint(0,maze.get_rows()-1))
        end = (random.randint(0,maze.get_rows()-1), random.randint(0,maze.get_rows()-1))
        return (start,end)