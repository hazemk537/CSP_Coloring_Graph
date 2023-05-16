# CSP_Coloring_Graph

```
Traceback (most recent call last):
  File "/home/up-user/Downloads/Projects/AICSP/index.py", line 22, in <module>
    solution = problem.solve()
  File "/home/up-user/Downloads/Projects/AICSP/solver.py", line 12, in solve
    self.backtrack(assignments)
  File "/home/up-user/Downloads/Projects/AICSP/solver.py", line 22, in backtrack
    if self.is_consistent(variable, value, assignments):
  File "/home/up-user/Downloads/Projects/AICSP/solver.py", line 40, in is_consistent
    if not self.is_satisfied(constraint,assignments):
  File "/home/up-user/Downloads/Projects/AICSP/solver.py", line 8, in is_satisfied
    return  assignments[constraint[0]]!=assignments[constraint[1]]
KeyError: 'NT'

```
