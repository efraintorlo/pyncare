import numpy as np


def plot_circle(ax, z=0.0, color='k', line_width=2):
    """Plot a circle in 3D plots
    to visualize the constraint"""
    X = np.linspace(-1, 1, 200)
    Y = np.sqrt(1.0 - X**2.0)
    Z = z
    ax.plot(X, Y, Z, color, linewidth=line_width)


def plot_circle_2D(ax, color='k', line_width=2):
    """Plot a circle in 2D plots
    to visualize the constraint"""
    X = np.linspace(-1, 1, 200)
    Y = np.sqrt(1.0 - X**2.0)
    ax.plot(X, Y, color, linewidth=line_width)


def plot_cylinder(ax, z_min=-1.0, z_max=0.5, color='r', alpha=0.2):
    """
    Plot a cylinder in 3D plots, this represents the constraint
    ARGS:
        ax (plt.ax):
        z_max (int):
        color (str):
        alpha (int:)
    """
    x = np.linspace(-1, 1, 100)
    z = np.linspace(z_min, z_max, 100)
    Xc, Zc = np.meshgrid(x, z)
    Yc = np.sqrt(1-Xc**2)
    # ax.plot_surface(Xc, Yc, Zc, rstride=20, cstride=10, color='0.8',
    #                 linewidth=0.0, alpha=0.2, antialiased=False)
    ax.plot_surface(Xc, Yc, Zc, color=color, rstride=20, cstride=5,
                    linewidth=0.0, alpha=alpha, antialiased=False)
