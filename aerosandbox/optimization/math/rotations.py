from aerosandbox.optimization.math.linalg import norm, outer
import numpy as np
import casadi as cas


def rotation_matrix_2D(
        angle,
):
    """
    Gives the 2D rotation matrix associated with a counterclockwise rotation about an angle.
    Args:
        angle: Angle by which to rotate. Given in radians.

    Returns: The 2D rotation matrix

    """
    sintheta = np.sin(angle)
    costheta = np.cos(angle)
    rotation_matrix = np.array([
        [costheta, -sintheta],
        [sintheta, costheta]
    ])
    return rotation_matrix


def rotation_matrix_angle_axis(
        angle,
        axis,
        _axis_already_normalized=False
):
    """
    Gives the 3D rotation matrix from an angle and an axis.
    An implmentation of https://en.wikipedia.org/wiki/Rotation_matrix#Rotation_matrix_from_axis_and_angle
    :param angle: can be one angle or a vector (1d ndarray) of angles. Given in radians. # TODO note deprecated functionality; must be scalar
        Direction corresponds to the right-hand rule.
    :param axis: a 1d numpy array of length 3 (x,y,z). Represents the angle.
    :param _axis_already_normalized: boolean, skips normalization for speed if you flag this true.
    :return:
        * If angle is a scalar, returns a 3x3 rotation matrix.
        * If angle is a vector, returns a 3x3xN rotation matrix.
    """
    if not _axis_already_normalized:
        axis = axis / norm(axis)

    sintheta = np.sin(angle)
    costheta = np.cos(angle)
    cpm = np.array([
        [0, -axis[2], axis[1]],
        [axis[2], 0, -axis[0]],
        [-axis[1], axis[0], 0],
    ])  # The cross product matrix of the rotation axis vector
    outer_axis = outer(axis, axis)

    rot_matrix = costheta * np.eye(3) + sintheta * cpm + (1 - costheta) @ outer_axis
    return rot_matrix

if __name__ == '__main__':
    rotation_matrix_angle_axis(0, cas.MX([1, 0, 1]))
