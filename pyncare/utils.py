import numpy as np


def plot_sphere(ax, phi_i=0, phi_f=2.0*np.pi,
                theta_i=0, theta_f=np.pi/2, res=50, **kwargs):
    """docstring for plot_3D_sphere_surface
    Plot two regions in the sphere"""
    if kwargs is not None and 'color' in kwargs:
        color = kwargs['color']
    else:
        color = '0.7'
    if kwargs is not None and 'alpha' in kwargs:
        alpha = kwargs['alpha']
    else:
        alpha = '1.0'

    phi = np.linspace(phi_i, phi_f, res)
    theta = np.linspace(theta_i, theta_f, res)
    x = 1 * np.outer(np.cos(phi), np.sin(theta))
    y = 1 * np.outer(np.sin(phi), np.sin(theta))
    z = 1 * np.outer(np.ones(np.size(phi)), np.cos(theta))
    ax.plot_surface(x, y, z, rstride=1, cstride=1, color=color,
                    linewidth=0.0, alpha=alpha, antialiased=False)


def plot_latitude(ax, theta_0=np.pi/4, r=1.0, phi_i=0, phi_f=2.0*np.pi, res=50, **kwargs):
    """plot a Parallel over the unit sphere"""

    phi = np.linspace(phi_i, phi_f, res)
    theta = theta_0
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.ones(res) * np.cos(theta)
    ax.plot(x, y, z, **kwargs)


def plot_quiver_2D(ax, x, y, u, v, **kwargs):
    if kwargs is not None and 'angles' in kwargs:
        angles = kwargs['angles']
    else:
        angles = 'xy'
    if kwargs is not None and 'scale_units' in kwargs:
        scale_units = kwargs['scale_units']
    else:
        scale_units = 'xy'
    if kwargs is not None and 'color' in kwargs:
        color = kwargs['color']
    else:
        color = 'k'
    if kwargs is not None and 'pivot' in kwargs:
        pivot = kwargs['pivot']
    else:
        pivot = 'mid'
    if kwargs is not None and 'scale' in kwargs:
        scale = kwargs['scale']
    else:
        scale = None
    if kwargs is not None and 'width' in kwargs:
        width = kwargs['width']
    else:
        width = 0.003
    if kwargs is not None and 'headlength' in kwargs:
        headlength = kwargs['headlength']
    else:
        headlength = 7
    if kwargs is not None and 'headwidth' in kwargs:
        headwidth = kwargs['headwidth']
    else:
        headwidth = 5

    if kwargs is not None and 'norm' in kwargs:
        norm = kwargs['norm']
    else:
        norm = True
    if kwargs is not None and 'rescale' in kwargs:
        rescale = kwargs['rescale']
    else:
        rescale = 1.0

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
    if kwargs is not None and 'color' in kwargs:
        color = kwargs['color']
    else:
        color = 'k'
    if kwargs is not None and 'length' in kwargs:
        length = kwargs['length']
    else:
        length = 0.05
    if kwargs is not None and 'arrow_length_ratio' in kwargs:
        arrow_length_ratio = kwargs['arrow_length_ratio']
    else:
        arrow_length_ratio = 1
    if kwargs is not None and 'linewidths' in kwargs:
        linewidths = kwargs['linewidths']
    else:
        linewidths = 1.0
    if kwargs is not None and 'norm' in kwargs:
        norm = kwargs['norm']
    else:
        norm = True
    if kwargs is not None and 'rescale' in kwargs:
        rescale = kwargs['rescale']
    else:
        rescale = 1.0

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
