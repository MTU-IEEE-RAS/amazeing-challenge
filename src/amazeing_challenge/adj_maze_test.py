from .mazes.adjacency_list_maze import AdjacencyListMaze
from .generators.aldous_broder_generator import AldousBroderGenerator
from .generators.wilsons_generator import WilsonsGenerator

generator = WilsonsGenerator()

maze = generator.generate_maze(9,5,5)

maze.print_maze()
print(generator.generate_start_and_goal(maze))

print(maze.get_edges((0,1)))