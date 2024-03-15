def unify(x, y, theta):
    if theta is None:
        return None
    elif x == y:
        return theta
    elif isinstance(x, str) and x.startswith('?'):
        return unify_var(x, y, theta)
    elif isinstance(y, str) and y.startswith('?'):
        return unify_var(y, x, theta)
    elif isinstance(x, list) and isinstance(y, list):
        return unify(x[1:], y[1:], unify(x[0], y[0], theta))
    else:
        return None

def unify_var(var, x, theta):
    if var in theta:
        return unify(theta[var], x, theta)
    elif x in theta:
        return unify(var, theta[x], theta)
    elif occur_check(var, x, theta):
        return None
    else:
        theta[var] = x
        return theta

def occur_check(var, x, theta):
    if var == x:
        return True
    elif isinstance(x, str) and x.startswith('?'):
        if var in theta:
            return occur_check(var, theta[x], theta)
    elif isinstance(x, list):
        return any(occur_check(var, xi, theta) for xi in x)
    return False

x = ['?x', 'is', 'red']
y = ['apple', 'is', '?y']
theta = {}
result = unify(x, y, theta)
print(result)
