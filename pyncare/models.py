import numpy as np


def compact_dyn_sys_phi2(init, t=None, model_pars=[]):
        '''
        This is the system dy_i/dt = f(y_i)
        This is the dynamical system defined for the model:
        $ V = m^2 \phi^2 / 2 $ inflation
        which have been rewritten in compactified variables
        over the Poncare Sphere using a central projection
        '''
        if t is None:
            t = 1.0  # This is used to allows a call from "plot_vector_flow()"

        X = init[0]
        Y = init[1]
        # the model equations
        Z = np.sqrt(1.0 - X**2.0 - Y**2.0)
        A = 3.0 * Y * np.sqrt(X**2.0 + Y**2.0) / Z
        X_dot = Y + X * Y * A
        Y_dot = -X + (Y**2.0 - 1.0) * A
        return [X_dot, Y_dot]


def dyn_sys_exp_yukawa_bounded(init, t=None, model_pars=[3.0, 0.0]):
    """Quintessence + Yukawa interaction (bounded vars)"""
    lambda1 = model_pars[0]
    r = model_pars[1]

    x = init[0]
    y = init[1]
    u = init[2]

    w_m = 0.0

    if u > 0.0:
        g = (1.0 - u)
        f = r * g / (1.0 - 2.0*u)
    else:
        g = (1.0 + u)
        f = r * g

    A = (1.0 - w_m) * x**2.0 + (1.0 + w_m)*(1.0 - y**2.0)
    Q = np.sqrt(6.0) * f * (1.0 - x**2.0 - y**2.0) / 2.0

    x_dot = Q - 3.0 * x + lambda1 * np.sqrt(6.0) * y**2.0 / 2.0 + 1.5 * x * A
    y_dot = -lambda1 * np.sqrt(6.0) * x * y / 2.0 + 1.5 * y * A
    u_dot = np.sqrt(6.0) * r * g**2.0 * x

    return [x_dot, y_dot, u_dot]
