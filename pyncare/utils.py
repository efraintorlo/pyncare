#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    File:        utils.py
    Author:      Efrain Torres-Lomas
    Email:       efrain@fisica.ugto.mx
    Github:      https://github.com/elchinot7
    Description: Some generic functions used in Pyncare
"""

import numpy as np


def plot_sphere(ax, phi_i=0, phi_f=2.0*np.pi,
                theta_i=0, theta_f=np.pi/2, res=50, r=1, **kwargs):
    """
    docstring for plot_3D_sphere_surface
    Plot two regions in the sphere
    """
    color = kwargs.get('color', '0.7')
    alpha = kwargs.get('alpha', '1.0')

    phi = np.linspace(phi_i, phi_f, res)
    theta = np.linspace(theta_i, theta_f, res)
    x = r * np.outer(np.cos(phi), np.sin(theta))
    y = r * np.outer(np.sin(phi), np.sin(theta))
    z = r * np.outer(np.ones(np.size(phi)), np.cos(theta))
    ax.plot_surface(x, y, z, rstride=1, cstride=1, color=color,
                    linewidth=0.0, alpha=alpha, antialiased=False)


def plot_latitude(ax, theta_0=np.pi/4, r=1.0, phi_i=0, phi_f=2.0*np.pi, res=50, **kwargs):
    """
    plot a Parallel over the unit sphere
    """
    phi = np.linspace(phi_i, phi_f, res)
    theta = theta_0
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.ones(res) * np.cos(theta)
    ax.plot(x, y, z, **kwargs)


def plot_circle(ax, r=1, theta_i=0, theta_f=2.0*np.pi, res=50, **kwargs):
    theta = np.linspace(theta_i, theta_f, res)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    ax.plot(x, y, **kwargs)


def plot_quiver_2D(ax, x, y, u, v, **kwargs):
    """
    Generic vector field flow  plotter
    """
    angles = kwargs.get('angles', 'xy')

    scale_units = kwargs.get('scale_units', 'xy')

    color = kwargs.get('color', 'k')

    pivot = kwargs.get('pivot', 'mid')

    scale = kwargs.get('scale', None)

    width = kwargs.get('width', 0.003)

    headlength = kwargs.get('headlength', 7)

    headwidth = kwargs.get('headwidth', 5)

    norm = kwargs.get('norm', True)

    rescale = kwargs.get('rescale', 1.0)

    u = np.array(u)
    v = np.array(v)

    if norm:
        N = np.sqrt(u**2 + v**2)
        U, V = u/N, v/N
    else:
        U, V = u, v

    U *= rescale
    V *= rescale

    ax.quiver(x, y, U, V, angles=angles, scale_units=scale_units,
              color=color, pivot=pivot, scale=scale,
              width=width, headlength=headlength, headwidth=headwidth)


def plot_quiver_3D(ax, x, y, z, u, v, w, **kwargs):
    color = kwargs.get('color', 'k')

    length = kwargs.get('length', 0.05)

    arrow_length_ratio = kwargs.get('arrow_length_ratio', 1)

    linewidths = kwargs.get('linewidths', 1.0)

    norm = kwargs.get('norm', True)

    rescale = kwargs.get('rescale', 1.0)

    u = np.array(u)
    v = np.array(v)
    w = np.array(w)

    if norm:
        N = np.sqrt(u**2 + v**2 + w**2)
        U, V, W = u/N, v/N, w/N
    else:
        U, V, W = u, v, w

    U *= rescale
    V *= rescale
    W *= rescale

    ax.quiver(x, y, z, U, V, W, color=color, length=length,
              arrow_length_ratio=arrow_length_ratio, linewidths=linewidths)
