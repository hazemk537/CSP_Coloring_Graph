from index import *

# Define the problem

# Define the variables (regions) and their possible values (colors)
variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V']
values = ['r', 'g', 'b']

for variable in variables:
    problem.addVariable(variable, values)

# Define the constraints (adjacent regions cannot have the same color)
problem.addConstraint(lambda a, b: a != b, ('WA', 'NT'))
problem.addConstraint(lambda a, b: a != b, ('WA', 'SA'))
problem.addConstraint(lambda a, b: a != b, ('NT', 'SA'))
problem.addConstraint(lambda a, b: a != b, ('NT', 'Q'))
problem.addConstraint(lambda a, b: a != b, ('SA', 'Q'))
problem.addConstraint(lambda a, b: a != b, ('SA', 'NSW'))
problem.addConstraint(lambda a, b: a != b, ('SA', 'V'))
problem.addConstraint(lambda a, b: a != b, ('NSW', 'Q'))
problem.addConstraint(lambda a, b: a != b, ('NSW', 'V'))

problem = problem(variable,values,constraints)

# Solve the problem
solutions = problem.getSolutions()

# Print the solutions (each solution is a dictionary of variable-value pairs)
for solution in solutions:
    print(solution)