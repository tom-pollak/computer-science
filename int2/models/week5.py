import random

import numpy as np
import matplotlib.pyplot as plt
from typing import Type
from models.week_4 import linear_classify, perceptron_with_offset, e_n, loss, plot_separator


def test_normalise():
    def generate_vector():
        rows = random.randint(1,100)
        cols = random.randint(1,100)
        return np.array([[random.randint(1,100) for _ in range(cols)] for _ in range(rows)])

    for _ in range(100):
        x = generate_vector()
        print(x)
        assert normalise(x) == np.linalg.norm(x), "Failed: %s" % x

def normalise(x):
    """
    Something to do with distance
    :param x: vector to normalise
    :return: normalised vector
    """
    assert isinstance(x, np.array.__class__), "x must be an np.array"

    norm2 = 0
    for row in x:
        for elem in row:
            norm2 += elem ** 2
    return np.sqrt(norm2)



def signed_dist(x: np.ndarray, theta: np.ndarray, theta_0) -> float:
    """
    Returns the signed perpendicular distance from hyperplane to x
    (negative means point is underneath hyperplane)

    :param x: Point to find distance to
    :param theta: normal vector to the hyperplane
    :param theta_0: y-intercept
    :return: 
    """
    assert (
        x.T.shape[1] == theta.shape[0]
    ), "Array shapes x.T, theta must be compatible: %s, %s" % (x.T.shape, theta.shape)

    return (x.T @ theta + theta_0) / np.linalg.norm(x)


if __name__ == "__main__":
    data1 = np.array([[1, 1, 2, 2], [-1, 1, -1, 1]])
    data1_labels = np.array([[-1, 1, 1, -1]])
    theta, theta_0 = perceptron_with_offset(data1, data1_labels)
    result = e_n(linear_classify, data1, data1_labels, loss, theta, theta_0)
    fig, ax = plt.subplots()  # create an empty plot and retrieve the 'ax' handle
    ax.scatter(data1[0, :], data1[1, :], c=colors, marker="o")
    plot_separator(ax, theta, theta_0)
