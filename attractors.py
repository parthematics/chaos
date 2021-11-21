# This file contains the systems of differential equations used to define 12 of the strange attractor models.
def halvorsen_system(current_state, t, params):
    x, y, z = current_state
    dx_dt = -(params['alpha'] * x) - (4 * y) - (4 * z) - (y ** 2)
    dy_dt = -(params['alpha'] * y) - (4 * z) - (4 * x) - (z ** 2)
    dz_dt = -(params['alpha'] * z) - (4 * x) - (4 * y) - (x ** 2)
    return [dx_dt, dy_dt, dz_dt]

def lorenz_system(current_state, t, params):
    x, y, z = current_state
    dx_dt = params['sigma'] * (y - x)
    dy_dt = x * (params['rho'] - z) - y
    dz_dt = x * y - params['beta'] * z
    return [dx_dt, dy_dt, dz_dt]

def dadras_system(current_state, t, params):
    x, y, z = current_state
    dx_dt = y - (params['a'] * x) + (params['b'] * y * z)
    dy_dt = (params['c'] * y) - (x * z) + z
    dz_dt = (params['d'] * x * y) - (params['e'] * z)
    return [dx_dt, dy_dt, dz_dt]

def chen_system(current_state, t, params):
    x, y, z = current_state
    dx_dt = (params['alpha'] * x) - (y * z)
    dy_dt = (params['beta'] * y) + (x * z)
    dz_dt = (params['delta'] * z) + (x * y / 3)
    return [dx_dt, dy_dt, dz_dt]

def lorenz83_system(current_state, t, params):
    x, y, z = current_state
    dx_dt = -(params['a'] * x) - (y ** 2) - (z ** 2) + (params['a'] * params['f'])
    dy_dt = -y + (x * y) - (params['b'] * x * z) + params['g']
    dz_dt = -z + (params['b'] * x * y) + (x * z)
    return [dx_dt, dy_dt, dz_dt]

def rossler_system(current_state, t, params):
    x, y, z = current_state
    dx_dt = -(y + z)
    dy_dt = x + (params['a'] * y)
    dz_dt = params['b'] + z * (x - params['c'])
    return [dx_dt, dy_dt, dz_dt]

def rabinovich_fabrikant_system(current_state, t, params):
    x, y, z = current_state
    dx_dt = y * (z - 1 + (x ** 2)) + (params['gamma'] * x)
    dy_dt = x * ((3 * z) + 1 - (x ** 2)) + (params['gamma'] * y)
    dz_dt = -2 * z * (params['alpha'] + (x * y))
    return [dx_dt, dy_dt, dz_dt]

def sprott_system(current_state, t, params):
    x, y, z = current_state
    dx_dt = y + (params['a'] * x * y) + (x * z)
    dy_dt = 1 - (params['b'] * (x ** 2)) + (y * z)
    dz_dt = x - (x ** 2) - (y ** 2)
    return [dx_dt, dy_dt, dz_dt]

def four_wing_system(current_state, t, params):
    x, y, z = current_state
    dx_dt = (params['a'] * x) + (y * z)
    dy_dt = (params['b'] * x) + (params['c'] * y) - (x * z)
    dz_dt = -z - (x * y)
    return [dx_dt, dy_dt, dz_dt]

system_map = {
    'halvorsen' : halvorsen_system,
    'lorenz' : lorenz_system,
    'dadras' : dadras_system,
    'chen' : chen_system,
    'lorenz83' : lorenz83_system,
    'rossler' : rossler_system,
    'rabinovich_fabrikant' : rabinovich_fabrikant_system,
    'sprott' : sprott_system,
    'four_wing' : four_wing_system
}

