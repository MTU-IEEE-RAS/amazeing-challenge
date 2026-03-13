import time
from .contracts import Generator, Solver, Maze


class Tester:

    def __init__(self, generator : Generator, solver : Solver, verbose : bool):
        self.generator = generator
        self.solver = solver
        self.verbose = verbose

    def report_failure(self):
        if self.verbose:
                print("Solution invalid!")

        return (False,-1)

    def validate_solution(self, maze : Maze, start, goal, solution : list) -> tuple:

        if len(solution) < 1:
            return self.report_failure()
            

        if start != solution[0] or goal != solution[-1]:
            return self.report_failure()

        for i in range(0,len(solution)-1):
            if not maze.has_edge(solution[i],solution[i+1]):
                return self.report_failure()

        # Don't count starting point as a step
        path_length = len(solution) - 1
        return (True, path_length)

    def test(self) -> dict:
        # Generate maze
        maze = self.generator.generate_maze()
        (start,goal) = self.generator.generate_start_and_goal(maze)

        # Solve maze, measure time elapsed
        start_time = time.perf_counter()
        results = []
        try:
            while True:
                solution = next(iter(self.solver.solve(maze, start, goal)))
                end_time = time.perf_counter()
                results.append({"solution": solution,
                                "end_time": end_time})
        except StopIteration as e:
            pass
            # Finished iterating!

        evals = []
        for result in results:
            # Check validity of solution, generate statistics
            (is_valid_solution, path_length) = self.validate_solution(maze,start,goal,result["solution"])
            time_elapsed = result["end_time"] - start_time

            evaluation = {'maze' : maze,
                    'solution' : result["solution"],
                    'is_valid_solution' : is_valid_solution,
                    'time_elapsed' : time_elapsed,
                    'path_length' : path_length}

            if self.verbose and evaluation['is_valid_solution']:
                print(f"Elapsed Time:  {results['time_elapsed']}")
                print(f"Path Length:   {results['path_length']}")
            evals.append(evaluation)

        return evals