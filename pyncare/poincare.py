#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    File:        poincare.py
    Author:      Efrain Torres-Lomas
    Email:       efrain@fisica.ugto.mx
    Github:      https://github.com/elchinot7
    Description: ToDo

"""
import numpy as np
from itertools import cycle
from dynsysbase import BaseDynSys
from utils import plot_sphere
from utils import plot_latitude


# def project_on_poincare(model):
#     def projection(**kwargs):
#         model_field = model(**kwargs)
#         X = model_field[0]
#         Y = model_field[1]
#         Z = 1.0 - X**2.0 - Y**2.0
#         return [X, Y, Z]
#     return projection


class PoincareCompact(BaseDynSys):

    def __init__(self, **kwargs):
        super(PoincareCompact, self).__init__(**kwargs)

    def plot_orbits(self, ax, vars_to_plot=['x', 'y'], colors=None, **kwargs):
        if colors is None:
            colorcycler = cycle(self.colors)
        else:
            colorcycler = cycle(colors)

        for i, orb in enumerate(self._orbits):
            color = next(colorcycler)
            orb.plot_function(ax=ax, indep_vars=vars_to_plot,
                              # flow_index=self.orbits[i]['arrow_pos'],
                              function=self.sphere_z,
                              # args=['x', 'y'],
                              color=color,
                              **kwargs
                              )
            orb.plot_flow_over_function(ax, indep_vars=vars_to_plot,
                                        function=self.sphere_z,
                                        function_dot=self.sphere_z_dot,
                                        flow_index=self.orbits[i]['arrow_pos'],
                                        width=0.03,
                                        color=color,
                                        )
            ax.set_xlabel(self.var_names[vars_to_plot[0]])
            ax.set_ylabel(self.var_names[vars_to_plot[1]])
            ax.set_zlabel(r'$Z$')

    def sphere_z(self, args):
        x = np.array(args[0])
        y = np.array(args[1])
        return np.sqrt(1.0 - x**2.0 - y**2.0)

    def sphere_z_dot(self, args):
        x = np.array(args[0])
        y = np.array(args[1])
        z = self.sphere_z([x, y])
        u, v = self.model([x, y])
        # return np.sqrt(- 2.0 * x * u - 2.0 * y * v)
        return (- x * u - y * v)/z

    def plot_poincare_surface(self, ax, phi_i=0, phi_f=2.0*np.pi,
                              theta_i=0, theta_f=np.pi/2, res=50, **kwargs):
        plot_sphere(ax=ax, theta_i=theta_i, theta_f=theta_f,
                    phi_i=phi_i, phi_f=phi_f,
                    res=res, **kwargs)

    def plot_equator(self, ax, is_projection=False, res=20, **kwargs):
        if is_projection:
            plot_latitude(ax, theta_0=np.pi/2, r=1.0, res=res, **kwargs)
        else:
            plot_latitude(ax, theta_0=np.pi/2, r=1.0, res=res, **kwargs)


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    from collections import OrderedDict
    from models import compact_dyn_sys_phi2
    # from utils import plot_latitude

    fig = plt.figure()
    # ax = fig.add_subplot(111)
    ax = Axes3D(fig)

    t = np.linspace(0.0, 50.0, 1000)

    var_names = {'x': r'$X$', 'y': r'$Y$', 'z': r'$Z$'}
    y0 = 0.5
    orbits = [{'vars': OrderedDict([('x', -0.8), ('y', y0)]), 't': t,
               'arrow_pos': [1, 100, 200], 'label': 'label0'},
              # {'vars': OrderedDict([('x', -0.6), ('y', y0)]), 't': t, 'arrow_pos': [5, 10, -10], 'label': 'label1'},
              # {'vars': OrderedDict([('x', -0.4), ('y', y0)]), 't': t, 'arrow_pos': [5, 10, -10], 'label': 'label2'},
              # {'vars': OrderedDict([('x', -0.2), ('y', y0)]), 't': t, 'arrow_pos': [5, 10, -10], 'label': 'label3'},
              # {'vars': OrderedDict([('x', 0.0), ('y', y0)]), 't': t, 'arrow_pos': [5, 10, -10], 'label': 'label4'},
              ]
    orbits += [{'vars': OrderedDict([('x', -0.8), ('y', y0)]), 't': -t, 'arrow_pos': [1], 'label': 'label0'},
               # {'vars': OrderedDict([('x', -0.6), ('y', y0)]), 't': -t, 'arrow_pos': [5, 10, -10], 'label': 'label1'},
               # {'vars': OrderedDict([('x', -0.4), ('y', y0)]), 't': -t, 'arrow_pos': [5, 10, -10], 'label': 'label2'},
               # {'vars': OrderedDict([('x', -0.2), ('y', y0)]), 't': -t, 'arrow_pos': [5, 10, -10], 'label': 'label3'},
               # {'vars': OrderedDict([('x', 0.0), ('y', y0)]), 't': -t, 'arrow_pos': [5, 10, -10], 'label': 'label4'},
               ]

    dynsys = PoincareCompact(model=compact_dyn_sys_phi2,
                             model_pars=[],
                             var_names=var_names,
                             Ndim=2,
                             orbits=orbits,
                             lines=None,
                             # colors='bright',
                             colors='black',
                             )
    print dynsys
    # print dynsys._orbits
    dynsys.plot_orbits(ax=ax, vars_to_plot=['x', 'y'])

    dynsys.plot_poincare_surface(ax, phi_i=0, phi_f=2*np.pi, theta_i=0, theta_f=np.pi/4,
                                 res=10, color='0.9', alpha=0.3)
    dynsys.plot_poincare_surface(ax, phi_i=0, phi_f=2*np.pi, theta_i=np.pi/4,
                                 theta_f=np.pi/2, res=10, color='g', alpha=0.3)

    dynsys.plot_equator(ax, ls='-', lw=2, is_projection=False)
    plot_latitude(ax, theta_0=np.pi/4, res=20, lw=2, color='k')
    plt.show()
