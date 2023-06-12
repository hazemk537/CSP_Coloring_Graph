from solver import *

# Define the problem
# Define the variables (regions) and their possible values (colors)
variables = ['Western Australia', 'Northern Territory', 'South Australia', 'Queensland', 'New South Wales',
             'Victoria', 'Tasmania']
# Australia Regions
domains = {
    'Western Australia': ['R', 'G', 'B', 'Y'],
    'Northern Territory': ['R', 'G', 'B', 'Y'],
    'South Australia': ['R', 'G', 'B', 'Y'],
    'Queensland': ['R', 'G', 'B', 'Y'],
    'New South Wales': ['R', 'G', 'B', 'Y'],
    'Victoria': ['R', 'G', 'B', 'Y'],
    'Tasmania': ['R', 'G', 'B', 'Y']
}

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
print("after Filtirng Using Forward Checking")

solution = problem.solve()
