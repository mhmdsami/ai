def satisfies_constraint(node1, color1, node2, color2, vars, adjacency_matrix):
    return color1 != color2 or not adjacency_matrix[vars.index(node1)][vars.index(node2)] == 1

def select_unassigned_variable(assignment, vars):
    for var in vars:
        if var not in assignment:
            return var
        
def csp(assignment, vars, colors, adjacency_matrix):
    if len(assignment) == len(vars):
        return assignment
    var = select_unassigned_variable(assignment, vars)
    for color in colors:
        if all(satisfies_constraint(var, color, assigned_var, assignment[assigned_var], vars, adjacency_matrix) for assigned_var in assignment):
            assignment[var] = color
            result = csp(assignment, vars, colors, adjacency_matrix)
            if result is not None:
                return result
            del assignment[var]

if __name__ == '__main__':
    adjacency_matrix = [
        [0, 1, 1, 0, 0 ,0], # Western Australia
        [1, 0, 1, 1, 0, 0], # Northern Territory
        [1, 1, 0, 1, 1, 1], # South Australia
        [0, 1, 1, 0, 1, 0], # Queensland
        [0, 0, 1, 1, 0, 1], # New South Wales
        [0, 0, 1, 0, 1, 0]  # Victoria
    ]

    colors = ['red', 'green', 'blue']
    states = ['Western Australia', 'Northern Territory', 'South Australia', 'Queensland', 'New South Wales', 'Victoria']
    solution = csp({}, states, colors, adjacency_matrix)
    print(solution)
