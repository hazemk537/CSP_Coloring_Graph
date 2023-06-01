import random
import matplotlib.pyplot as plt
import geopandas
import copy
class Problem:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.constraints = constraints
        self.domains=domains

    def solve(self):
        assignments = {}
        self.backtrack(assignments)
        self.map_plot(assignments)
        return assignments
    def forward_check(self, variable, value, assignments):
        remaining_domains = {}
        for constraint in self.constraints:
            if (constraint[0] == variable and constraint[1] not in assignments) :
                if value in self.domains[variable]:
                    self.domains[variable].remove(value)
                    remaining_domains[constraint[1]] = self.domains[variable][:]
                if not self.domains:
                    return None
        return remaining_domains

    def backtrack(self, assignments):
        if len(assignments) == len(self.variables):
            print(len(assignments),"in the backTrack")
            return True


        variable = self.select_unassigned_variable(assignments)
        for value in self.domains[variable]:
            if self.is_consistent(variable, value, assignments):
                remaining_domains = self.forward_check(variable, value, assignments)
                if remaining_domains is not None:  # Check for None instead of False
                    if self.backtrack(assignments):
                        return True
                else:
                  del assignments[variable]
                  self.undo_forward_check(remaining_domains)
                  return False
    def undo_forward_check(self, remaining_domains):
     if remaining_domains is not None:
        for variable, domain in remaining_domains.items():
            self.domains = domain


    def select_unassigned_variable(self, assignments):
        unassigned_variables=[] #NOTE append to unassignedList and select Randomly
        for variable in self.variables:
            if variable not in assignments:
                unassigned_variables.append(variable)
        randomNumber=random.randint(0,len(unassigned_variables)-1)#inclusive
        return unassigned_variables[randomNumber]

    def is_satisfied(self, constraint, assignments):  # given constrains in pairs should never be equal
        if (constraint[0] in assignments) and (constraint[1] in assignments):
            return assignments[constraint[0]] != assignments[constraint[1]]
        return True

    def is_consistent(self, variable, value, assignments):
        assignments[variable] = value#3. try assign selected var to selected value

        for constraint in self.constraints:#4. check all avialable constriants
            if  not self.is_satisfied(constraint, assignments):
                del assignments[variable]#5. if any Constraint is broke
                return False
        return True#6. if all constraints are well !

    def map_plot(self, soulation):
        print("Ready to plot map for AUS")
        path = "./aus_basic/"
        # # load the shape file using geopandas
        states = geopandas.read_file(path + 'STE_2016_AUST.shp')
        states = states.to_crs("EPSG:3395")
        ax2 = states.boundary.plot(figsize=(12, 12), edgecolor=u'gray')
        if soulation is not None:
            for k, v in soulation.items():
                if v == 'R':
                    states[states.STE_NAME16 == k].plot(edgecolor=u'gray', color='red', ax=ax2)
                elif v == 'B':
                    states[states.STE_NAME16 == k].plot(edgecolor=u'gray', color='blue', ax=ax2)
                elif v == 'G':
                    states[states.STE_NAME16 == k].plot(edgecolor=u'gray', color='green', ax=ax2)
                else:
                    states[states.STE_NAME16 == k].plot(edgecolor=u'gray', color='yellow', ax=ax2)

            plt.show()
