from ..contracts import Generator, Maze
from ..mazes.adjacency_list_maze import AdjacencyListMaze
import random

# Implements Wilson's Algorithm (https://weblog.jamisbuck.org/2011/1/20/maze-generation-wilson-s-algorithm)
class WilsonsGenerator(Generator):

    def generate_maze(self,seed=None,rows=5,cols=5) -> Maze:
        # Initialize
        maze = AdjacencyListMaze(rows,cols)
        unvisited = maze.get_nodes()
        ust = []

        if seed != None:
            random.seed(seed)

        current_node = unvisited[random.randint(0,len(unvisited)-1)]
        unvisited.remove(current_node)
        ust.append(current_node)

        # Random Walk
        reset_walk = True
        while(len(ust) < len(maze.get_nodes())):
            if reset_walk:
                current_node = unvisited[random.randint(0,len(unvisited)-1)]
                random_walk = [current_node]
                reset_walk = False

            neighbors = maze.get_node_neighbors(current_node)
            neighbor = neighbors[random.randint(0,len(neighbors)-1)]

            if neighbor in ust:
                
                random_walk.append(neighbor)

                # Add edges to maze and ust
                for i in range(len(random_walk)-1):
                    maze.add_edge(random_walk[i],random_walk[i+1])
                
                for n in random_walk[:-1]: # Last node is already in UST
                    unvisited.remove(n)
                    ust.append(n)

                # Exit once all nodes are in UST
                if len(ust) == len(maze.get_nodes()):
                    return maze

                # Reset walk for next iteration
                reset_walk = True

            if not reset_walk:
                if neighbor in random_walk:
                    if neighbor == random_walk[0]:
                        random_walk = [neighbor]
                    else:
                        random_walk = random_walk[0:random_walk.index(neighbor)+1]
                else:
                    random_walk.append(neighbor)

                current_node = neighbor

        return None
        
    def generate_start_and_goal(self,maze : Maze) -> tuple:
        start = (random.randint(0,maze.get_rows()-1), random.randint(0,maze.get_cols()-1))
        end = (random.randint(0,maze.get_rows()-1), random.randint(0,maze.get_cols()-1))
        return (start,end)