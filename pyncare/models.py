import numpy as np

def compact_dyn_sys_phi2(init, t=None, modelpars=[]):
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
