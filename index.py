from solver import *
# Define the problem
# Define the variables (regions) and their possible values (colors)
variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V'] #Australia Regions
#https://2.bp.blogspot.com/-9mXaXVUbPHQ/T8CYBASTQ4I/AAAAAAAACIo/cW09mus4IEg/s760/australia-map-picture.gif
domains = ['r', 'g', 'b']
constraints=[
 ('WA', 'NT'),
 ('WA', 'SA'),
 ('NT', 'SA'),
 ('NT', 'Q'),
 ('SA', 'Q'),
 ('SA', 'NSW'),
 ('SA', 'V'),
 ('NSW', 'Q'),
 ('NSW', 'V')]


problem = Problem(variables,domains,constraints)


# Solve the problem
solution = problem.solve()
print(solution)


