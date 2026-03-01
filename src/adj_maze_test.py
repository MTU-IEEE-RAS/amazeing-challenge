from mazes.adjacency_list_maze import AdjacencyListMaze
from generators.aldous_broder_generator import AldousBroderGenerator

generator = AldousBroderGenerator()

maze = generator.generate_maze(5,5)

maze.print_adjacency_list()
maze.print_maze()
print(generator.generate_start_and_goal(maze))