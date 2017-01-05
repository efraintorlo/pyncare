# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File:        orbit.py
Author:      Efrain Torres-Lomas
Email:       efrain@fisica.ugto.mx
Github:      https://github.com/elchinot7
Description: This contains the more basic class in the package, namely, the
             Orbit. This class define a orbit ( a solution ) for the generic
             dynamical system. Orbit is able to be integrated (evolved) and
             plotted.

"""
import numpy as np
from scipy.integrate import odeint
import sys
from utils import plot_quiver_2D, plot_quiver_3D
from utils import  plot_quiver_fancy_2D

_arrow_style = "quiver"
#_arrow_style = "fancy"



class Orbit(object):
    """Orbit is the fundamental class in Pyncare."""

    def __init__(self, init_cond, model, model_pars, t, label='orbit'):
        self.init_cond = init_cond  # must be an collections.OrderedDict
        self.names = list(init_cond.keys())
        self.init = list(init_cond.values())
        self.Ndim = len(init_cond)      # int
        self.model = model              # method
        self.model_pars = model_pars    # list
        self.t = t                      # numpy array
        self.label = label
        self.solution = []
        self.is_solved = False

    def __str__(self):
        return "{} is an {} object with init cond: {} = {}".format(self.label,
                                                                   self.__class__.__name__,
                                                                   self.names,
                                                                   self.init)

    def evolve(self, t=None):
        if self.is_solved:
            pass
        if t is None:
            t = self.t
        self.solution = odeint(self.model, self.init, t=t, args=(self.model_pars,))
        self.is_solved = True

    def plot_orbit(self, ax, vars_to_plot, **kwargs):
        if len(vars_to_plot) > 3:
            sys.exit("We can't plot in Ndim > 3")

        if not all(key in self.names for key in vars_to_plot):  # check vars to plot exist
            sys.exit("vars_to_plot are not a subset of vars")

        if kwargs is not None and 't' in kwargs:
            t = kwargs['t']
        else:
            t = None

        self.evolve(t=t)

        # plot_list = []
        indexes = []
        for key in vars_to_plot:
            ind = self.init_cond.keys().index(key)
            indexes.append(ind)

        if len(vars_to_plot) is 2:
            ax.plot(self.solution[:, indexes[0]], self.solution[:, indexes[1]], label=self.label, **kwargs)
        elif len(vars_to_plot) is 3:
            ax.plot(self.solution[:, indexes[0]], self.solution[:, indexes[1]], self.solution[:, indexes[2]],
                    label=self.label, **kwargs)

    def plot_function(self, ax, indep_vars, function, args=None, **kwargs):
        if args is not None and not all(key in self.names for key in args):  # check vars exist
            sys.exit("args are not a subset of vars")
        if not all(key in self.names for key in indep_vars):  # check indep_vars exist
            sys.exit("indep_vars are not a subset of vars")

        if kwargs is not None and 't' in kwargs:
            t = kwargs['t']
        else:
            t = None

        # Evolving...
        self.evolve(t=t)

        indep_vars_list = []
        for key in indep_vars:
            ind = self.init_cond.keys().index(key)
            indep_vars_list.append(self.solution[:, ind])

        if args is None:
            f = function([self.solution[:, 0], self.solution[:, 1]])
        else:
            args_list = []
            for key in args:
                ind = self.init_cond.keys().index(key)
                args_list.append(self.solution[:, ind])

            f = function(args_list)

        if len(indep_vars) == 1:
            x = indep_vars_list[0]
            ax.plot(x, f, **kwargs)
        elif len(indep_vars) == 2:
            x = indep_vars_list[0]
            y = indep_vars_list[1]
            ax.plot(x, y, f, **kwargs)

    def plot_flow_over_orbit(self, ax, vars_to_plot, flow_index=None, arrow_kws=None):

        if arrow_kws is None:
            arrow_kws = dict()

        if flow_index is None:
            sys.exit("flow_index must be a list of integers")
        if any(not isinstance(x, int) for x in flow_index):
            print type(flow_index)
            sys.exit("flow_index must be a list of integers")

        if not self.is_solved:
            sys.exit("To plot the flow you must plot the orbit solution first")

        indexes = []
        for key in vars_to_plot:
            ind = self.init_cond.keys().index(key)
            indexes.append(ind)

        vels = [self.model(init=self.solution[i], model_pars=self.model_pars) for i in flow_index if (i < len(self.solution[:, indexes[0]]))]
        # print 'vels = ', vels

        if len(indexes) > 1:
            x = np.array([self.solution[:, indexes[0]][i] for i in flow_index if (i < len(self.solution[:, indexes[0]]))])
            y = np.array([self.solution[:, indexes[1]][i] for i in flow_index if (i < len(self.solution[:, indexes[1]]))])

        if len(indexes) > 2:
            z = np.array([self.solution[:, indexes[2]][i] for i in flow_index if (i < len(self.solution[:, indexes[2]]))])

        if len(indexes) == 2:
            U = [vel[indexes[0]] for vel in vels]
            V = [vel[indexes[1]] for vel in vels]
            if _arrow_style is 'quiver':
                plot_quiver_2D(ax=ax, x=x, y=y, u=U, v=V, arrow_kws=arrow_kws)
            if _arrow_style is 'fancy':  # Not fully implemented
                plot_quiver_fancy_2D(ax=ax, x=x, y=y, u=U, v=V, **kwargs)

        elif len(indexes) == 3:
            U = [vel[indexes[0]] for vel in vels]
            V = [vel[indexes[1]] for vel in vels]
            W = [vel[indexes[2]] for vel in vels]
            if _arrow_style is 'quiver':
                plot_quiver_3D(ax=ax, x=x, y=y, z=z, u=U, v=V, w=W, arrow_kws=arrow_kws)

    def plot_flow_over_function(self, ax, indep_vars, function, function_dot,
                                flow_index, args=None, arrow_kws=None):
        if arrow_kws is None:
            arrow_kws = dict()

        if flow_index is None:
            sys.exit("flow_index must be a list of integers")
        if any(not isinstance(x, int) for x in flow_index):
            print type(flow_index)
            sys.exit("flow_index must be a list of integers")

        if not self.is_solved:
            sys.exit("To plot the flow you must plot the orbit solution first")

        indep_vars_list = []
        indexes = []
        for key in indep_vars:
            ind = self.init_cond.keys().index(key)
            indexes.append(ind)
            indep_vars_list.append(self.solution[:, ind])

        if self.Ndim > 0:
            x = np.array([self.solution[:, 0][i] for i in flow_index if (i < len(self.solution[:, 0]))])
        if self.Ndim > 1:
            y = np.array([self.solution[:, 1][i] for i in flow_index if (i < len(self.solution[:, 1]))])

        f = function([x, y])

        f_dot = function_dot([x, y])

        if self.Ndim == 2:
            U, V = zip(*[self.model(init=[x1, y1], model_pars=self.model_pars) for x1, y1 in zip(x, y)])

        if len(indep_vars) == 1:
            if _arrow_style is 'quiver':
                plot_quiver_2D(ax=ax, x=x, y=f, u=U, v=f_dot, arrow_kws=arrow_kws)

        if len(indep_vars) == 2:
            if _arrow_style is 'quiver':
                plot_quiver_3D(ax=ax, x=x, y=y, z=f, u=U, v=V, w=f_dot, arrow_kws=arrow_kws)


def test_model(init, t=None, model_pars=[]):
    r"""Dynamical system for model
    :math:`V = m^2 \phi^2/2`
    """
    x1 = init[0]
    y1 = init[1]
    # the model equations
    x1_dot = y1
    y1_dot = -x1 - 3.0 * y1 * np.sqrt(x1**2.0 + y1**2.0)
    return [x1_dot, y1_dot]


def test_function(args):
    x = args[0]
    y = args[1]
    return x + y**2 + y**3


def test_function_dot(args):
    x = args[0]
    y = args[1]
    u, v = test_model([x, y])
    return u + 2*y*v + (3*y**2)*v


if __name__ == "__main__":
    import collections
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(111)

    d0 = collections.OrderedDict()
    d0['x'] = 0
    d0['y'] = 1

    t = np.linspace(0.0, 1.0, 50)

    orbit = Orbit(init_cond=d0, model=test_model, model_pars=[], t=t,
                  label='The_Label')
    print orbit

    arrow_settings = {"angles": "xy",
                      "scale_units=": "xy",
                      "pivot": 'mid',
                      "scale": 1.0,
                      "width": 0.005,
                      "headlength": 5,
                      'headwidth': 5,
                      'norm': True,
                      'rescale': 0.1}

    orbit.plot_orbit(ax, vars_to_plot=['x', 'y'], lw=2, color='g')
    arrow_settings['color'] = 'g'
    orbit.plot_flow_over_orbit(ax, vars_to_plot=['x', 'y'], flow_index=[10, 20, 30, 40],
                               arrow_kws=arrow_settings)
    orbit.plot_function(ax, indep_vars=['x'], function=test_function,
                        label='function', color='r', linewidth=2)
    arrow_settings['color'] = 'r'
    orbit.plot_flow_over_function(ax, indep_vars=['x'], function=test_function,
                                  function_dot=test_function_dot,
                                  args=None, flow_index=[1, 3, 5, -2],
                                  arrow_kws=arrow_settings)
    ax.legend()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    plt.show()
