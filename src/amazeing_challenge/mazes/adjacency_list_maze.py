from ..contracts import Maze

class AdjacencyListMaze(Maze):
    def __init__(self,rows,cols):
        self.rows = rows
        self.cols = cols
        self.node_count = self.rows*self.cols
        self.adjacency_list = {}

        for i in range(self.node_count):
            self.adjacency_list[i] = [] 

    def add_edge(self, n1 : tuple, n2 : tuple):

        # Only add if nodes are neighbors
        if abs(n1[0] - n2[0]) + abs(n1[1]-n2[1]) > 1:
            print(f"Invalid edge, nodes {n1} and {n2} are not neighbors.")
            return 
        
        n1_idx = self.get_adj_list_idx(n1)
        n2_idx = self.get_adj_list_idx(n2)

        self.adjacency_list[n1_idx].append(n2_idx)
        self.adjacency_list[n2_idx].append(n1_idx)

    def get_adj_list_idx(self, n: tuple) -> int:
        return n[1] + n[0]*self.cols
    
    def get_edges(self,n:tuple) -> list:
        edges = []
        print(self.adjacency_list[self.get_adj_list_idx(n)])
        for v in self.adjacency_list[self.get_adj_list_idx(n)]:
            n2 = self.get_node_coordinate(v)
            edges.append([n,n2])

        return edges

    def get_rows(self) -> int:
        return self.rows
    
    def get_node_coordinate(self, v):
        return (v // self.cols, v % self.cols)

    def get_node_neighbors(self, n: tuple) -> list:
        neighbors = []

        left_idx = n[0] - 1
        right_idx = n[0] + 1
        up_idx = n[1] - 1
        down_idx = n[1] + 1

        if left_idx >= 0:
            neighbors.append((left_idx,n[1]))
        if right_idx < self.rows:
            neighbors.append((right_idx,n[1]))
        if up_idx >= 0:
            neighbors.append((n[0],up_idx))
        if down_idx < self.cols:
            neighbors.append((n[0],down_idx))

        return neighbors

    def get_nodes(self) -> list:

        node_list = []
        for i in range(self.node_count):
            node_list.append(self.get_node_coordinate(i))
        return node_list
    
    def get_cols(self) -> int:
        return self.cols

    def has_edge(self,n1:tuple, n2:tuple) -> bool:
        v1 = self.get_adj_list_idx(n1)
        v2 = self.get_adj_list_idx(n2)
        
        return v1 in self.adjacency_list[v2]
    
    def print_adjacency_list(self):
        for vertex, neighbors in self.adjacency_list.items():
            print(f"{vertex} -> {' '.join(map(str, neighbors))}")

    def print_maze(self):

        # The row and column numbers only print nicely for single digits for now...
        print_numbers = False
        if(self.cols < 10 and self.rows < 10):
            print_numbers = True
        
        wall = "██"
        path = "  "

        maze_string = "  "

        hor_border_string = "  "
        for i in range(self.cols*2+1):
            hor_border_string += wall
        hor_border_string += "\n"

        if(print_numbers):
            for i in range(self.cols):
                maze_string += f"  {i} "

        maze_string += "\n"

        maze_string += hor_border_string

        for i in range(self.rows):

            if(print_numbers):
                maze_string += f"{i} " + wall
            else:
                maze_string += "  " + wall

            # Check right neighbor
            for j in range(self.cols-1):
                maze_string += path

                if not self.has_edge((i,j),(i,j+1)):
                    maze_string += wall
                else:
                    maze_string += path

            maze_string += path + wall + "\n"

            # Check down neighbor
            if i >= self.rows-1:
                break

            maze_string += "  " + wall

            for j in range(self.cols):
                if not self.has_edge((i,j),(i+1,j)):
                    maze_string += wall
                else:
                    maze_string += path

                maze_string += wall

            maze_string += "\n"

        maze_string += hor_border_string

        print(maze_string)
    
    def remove_edge(self, n1 : tuple, n2 : tuple):
        self.adjacency_list[n1].remove(n2)