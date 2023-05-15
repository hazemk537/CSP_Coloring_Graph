class Problem:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def solve(self):
        assignments = {}
        self.backtrack(assignments)
        return assignments

    def backtrack(self, assignments):
        if len(assignments) == len(self.variables):
            return True

        variable = self.select_unassigned_variable(assignments)

        for value in self.order_domain_values(variable, assignments):
            if self.is_consistent(variable, value, assignments):
                assignments[variable] = value
                if self.backtrack(assignments):
                    return True
                del assignments[variable]

        return False

    def select_unassigned_variable(self, assignments):
        for variable in self.variables:
            if variable not in assignments:
                return variable

    def order_domain_values(self, variable, assignments):
        return self.domains[variable]

    def is_consistent(self, variable, value, assignments):
        assignments[variable] = value
        for constraint in self.constraints[variable]:
            if not constraint.is_satisfied(assignments):
                del assignments[variable]
                return False
        del assignments[variable]
        return True







        