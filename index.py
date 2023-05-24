from solver import Problem
# Define the problem
# Define the variables (regions) and their possible values (colors)
#MAP:::https://www.worldmap1.com/map-australia.asp
variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V']  # Australia Regions
domains = ['r', 'g', 'b']
constraints = [
    ('WA', 'NT'),
    ('WA', 'SA'),
    ('NT', 'SA'),
    ('NT', 'Q'),
    ('SA', 'Q'),
    ('SA', 'NSW'),
    ('SA', 'V'),
    ('NSW', 'Q'),
    ('NSW', 'V')]

problem = Problem(variables, domains, constraints)

# Solve the problem
solution = problem.solve()
print(solution)