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
from utils import plot_circle


class PoincareCompact(BaseDynSys):
    """Dyn Sys in Caompact coordinates."""

    def __init__(self, **kwargs):
        super(PoincareCompact, self).__init__(**kwargs)

    def plot_orbits(self, ax, vars_to_plot=['x', 'y'], add_flow=True,
                    colors=None, arrow_kws=None, **kwargs):
        if arrow_kws is None:
            arrow_kws = dict()

        if colors is None:
            colorcycler = cycle(self.colors)
        else:
            colorcycler = cycle(colors)

        for i, orb in enumerate(self._Orbits):
            color = next(colorcycler)
            orb.plot_function(ax=ax, indep_vars=vars_to_plot,
                              function=self.sphere_z,
                              color=color,
                              **kwargs
                              )
            if add_flow:
                arrow_kws['color'] = color
                orb.plot_flow_over_function(ax, indep_vars=vars_to_plot,
                                        function=self.sphere_z,
                                        function_dot=self.sphere_z_dot,
                                        flow_index=self.orbits[i]['arrow_pos'],
                                        arrow_kws=arrow_kws
                                        )
            ax.set_xlabel(self.var_names[vars_to_plot[0]])
            ax.set_ylabel(self.var_names[vars_to_plot[1]])
            ax.set_zlabel(r'$Z$')

    def plot_vertical_projection(self, ax, vars_to_plot=['x', 'y'], add_flow=True, colors=None,
                                 arrow_kws=None, **kwargs):
        if arrow_kws is None:
            arrow_kws = dict()

        if colors is None:
            colorcycler = cycle(self.colors)
        else:
            colorcycler = cycle(colors)

        for i, orb in enumerate(self._Orbits):
            color = next(colorcycler)
            orb.plot_orbit(ax=ax, vars_to_plot=vars_to_plot,
                           color=color,
                           **kwargs
                           )
            if add_flow:
                arrow_kws['color'] = color
                orb.plot_flow_over_orbit(ax, vars_to_plot=vars_to_plot,
                                         flow_index=self.orbits[i]['arrow_pos'], arrow_kws=arrow_kws)

            ax.set_xlabel(self.var_names[vars_to_plot[0]])
            ax.set_ylabel(self.var_names[vars_to_plot[1]])

    def sphere_z(self, args):
        X = np.array(args[0])
        Y = np.array(args[1])
        return np.sqrt(1.0 - X**2.0 - Y**2.0)

    def sphere_z_dot(self, args):
        X = np.array(args[0])
        Y = np.array(args[1])
        Z = self.sphere_z([X, Y])
        U, V = self.model([X, Y])
        return (- X * U - Y * V)/Z

    def plot_poincare_surface(self, ax, phi_i=0, phi_f=2.0*np.pi,
                              theta_i=0, theta_f=np.pi/2, res=50, r=1, **kwargs):
        plot_sphere(ax=ax, theta_i=theta_i, theta_f=theta_f,
                    phi_i=phi_i, phi_f=phi_f,
                    res=res, r=r, **kwargs)

    def plot_equator(self, ax, r=1.0, is_projection=False, res=50, **kwargs):
        if is_projection:
            plot_circle(ax, r=r, res=res, **kwargs)
        else:
            plot_latitude(ax, theta_0=np.pi/2, r=r, res=res, **kwargs)


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    from collections import OrderedDict
    from models import compact_dyn_sys_phi2

    fig = plt.figure()
    # ax = fig.add_subplot(111)
    ax = Axes3D(fig)

    t = np.linspace(0.0, 20.0, 500)
    t1 = np.linspace(0.0, 5.0, 500)

    var_names = {'x': r'$X$', 'y': r'$Y$', 'z': r'$Z$'}
    y0 = 0.5
    orbits = [{'vars': OrderedDict([('x', -0.8), ('y', y0)]), 't': t,
               'arrow_pos': [1, 100, 200], 'label': 'label0'},
              ]
    orbits += [{'vars': OrderedDict([('x', -0.8), ('y', y0)]), 't': -t1, 'arrow_pos': [1], 'label': 'label0'},
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

    arrow_settings_2d = {"angles": "xy",
                         "scale_units=": "xy",
                         "pivot": 'mid',
                         "scale": None,
                         "width": 0.005,
                         "headlength": 5,
                         'headwidth': 5,
                         'norm': True,
                         'rescale': 1.0,}

    arrow_settings_3d = {"linewidths": 2.0, "norm": True,
                      "length": 0.09, "arrow_length_ratio": 0.5,
                      "rescale": 1.0,
                      }

    dynsys.plot_orbits(ax=ax, vars_to_plot=['x', 'y'], arrow_kws=arrow_settings_3d)

    dynsys.plot_poincare_surface(ax, phi_i=0, phi_f=2*np.pi, theta_i=0, theta_f=np.pi/4,
                                 res=10, color='0.9', alpha=0.3)
    dynsys.plot_poincare_surface(ax, phi_i=0, phi_f=2*np.pi, theta_i=np.pi/4,
                                 theta_f=np.pi/2, res=10, color='g', alpha=0.3)

    dynsys.plot_equator(ax, ls='-', lw=2, is_projection=False)
    plot_latitude(ax, theta_0=np.pi/4, res=20, lw=2, color='k')

    fig_2d = plt.figure()
    ax_2d = fig_2d.add_subplot(111)

    dynsys.plot_vertical_projection(ax_2d, vars_to_plot=['x', 'y'], arrow_kws=arrow_settings_2d)
    dynsys.plot_equator(ax_2d, ls='-', res=100, lw=2, is_projection=True)
    plot_circle(ax_2d, r=0.5, ls='--', color='r')
    ax_2d.set_xlim(-1.1, 1.1)
    ax_2d.set_ylim(-1.1, 1.1)
    ax_2d.set_aspect('equal')
    plt.show()
