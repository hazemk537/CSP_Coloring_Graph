from solver import *

# Define the problem
# Define the variables (regions) and their possible values (colors)
variables = ['Western Australia', 'Northern Territory', 'South Australia', 'Queensland', 'New South Wales',
                 'Victoria', 'Tasmania']
    # Australia Regions
domains = ['R', 'G', 'B', "Y"]
constraints = [
        ('Western Australia', 'Northern Territory'),
        ('Western Australia', 'South Australia'),
        ('Northern Territory', 'South Australia'),
        ('Northern Territory', 'Queensland'),
        ('South Australia', 'Queensland'),
        ('South Australia', 'New South Wales'),
        ('South Australia', 'Victoria'),
        ('New South Wales', 'Queensland'),
        ('New South Wales', 'Victoria'),
        ('Tasmania', 'Victoria')
    ]
problem = Problem(variables, domains, constraints)

# Solve the problem
solution = problem.solve()
print(solution)
