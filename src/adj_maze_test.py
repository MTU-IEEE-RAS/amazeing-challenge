from mazes.adjacency_list_maze import AdjacencyListMaze
from generators.aldous_broder_generator import AldousBroderGenerator
from generators.wilsons_generator import WilsonsGenerator

generator = WilsonsGenerator()

maze = generator.generate_maze(20,20)

maze.print_adjacency_list()
maze.print_maze()
print(generator.generate_start_and_goal(maze))