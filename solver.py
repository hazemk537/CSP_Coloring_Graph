class Problem:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints #how list ?

    def is_satisfied (self,constraint,assignments): # given constrains in pairs should never be equal
       return  assignments[constraint[0]]!=assignments[constraint[1]]

    def solve(self):
        assignments = {}# canot represented by nCr,must be given
        self.backtrack(assignments)
        return assignments

    def backtrack(self, assignments):
        if len(assignments) == len(self.variables):
            return True

        variable = self.select_unassigned_variable(assignments)#find the unassigned var

        for value in self.order_domain_values(variable, assignments):
            if self.is_consistent(variable, value, assignments):
                assignments[variable] = value#?
                if self.backtrack(assignments):
                    return True
            del assignments[variable] #?

        return False

    def select_unassigned_variable(self, assignments):
        for variable in self.variables:
            if variable not in assignments:
                return variable

    def order_domain_values(self, variable, assignments):#domain should be changed automatically 
        return self.domains[variable]

    def is_consistent(self, variable, value, assignments):
        assignments[variable] = value
        for constraint in self.constraints:
            if not self.is_satisfied(constraint,assignments):
                del assignments[variable]
                return False
        del assignments[variable]#?
        return True







        