import numpy as np
import casadi as cas
from numpy import pi


def linspace(
        start: float = 0.,
        stop: float = 1.,
        n_points: int = 50
):
    """
    Makes a linearly-spaced vector.
    Args:
        start: Value to start at.
        stop: Value to end at.
        n_points: Number of points in the vector.
    """
    try:
        return np.linspace(start, stop, n_points)
    except Exception:
        return cas.linspace(start, stop, n_points)


def cosspace(
        start: float = 0.,
        stop: float = 1.,
        n_points: int = 50
):
    """
    Makes a cosine-spaced vector.

    To learn about cosine spacing, see this: https://youtu.be/VSvsVgGbN7I
    Args:
        start: Value to start at.
        end: Value to end at.
        n_points: Number of points in the vector.
    """
    mean = (stop + start) / 2
    amp = (stop - start) / 2
    return mean + amp * np.cos(np.linspace(pi, 0, n_points))
