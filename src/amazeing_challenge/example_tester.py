from generators.dummy_generator import DummyGenerator
from solvers.dummy_solver import DummySolver
from tester import Tester

generator = DummyGenerator()
solver = DummySolver()

tester = Tester(generator,solver,verbose=True)

tester.test()