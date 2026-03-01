from contracts import Generator, Maze
from mazes.adjacency_list_maze import AdjacencyListMaze
from random import randint

class AldousBroderGenerator(Generator):

    def generate_maze(self,length,width) -> Maze:
        maze = AdjacencyListMaze(length,width)

        unvisited = maze.get_nodes()

        current_node = unvisited[randint(0,len(unvisited)-1)]
        unvisited.remove(current_node)

        while len(unvisited) > 0:
            neighbors = maze.get_node_neighbors(current_node)

            neighbor = neighbors[randint(0,len(neighbors)-1)]

            if neighbor in unvisited:
                maze.add_edge(current_node,neighbor)
                unvisited.remove(neighbor)

            current_node = neighbor

            print(len(unvisited))

        return maze
        

    def generate_start_and_goal(self,maze : Maze) -> tuple:
        pass