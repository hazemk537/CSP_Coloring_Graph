def is_satisfied(self, variable, value, assignments):
    assignments[variable] = value
    for constraint in self.constraints[variable]:
        if not constraint(assignments):
            del assignments[variable]
            return False
    del assignments[variable]
    return True



# def different_colors_constraint(a, b):
#     return a != b