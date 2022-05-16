import numpy as np
import matplotlib.pyplot as plt

from models.week_4 import plot_separator


def perceptron(data, labels, params=None, hook=None):
	"""The Perceptron learning algorithm.

	:param data: A d x n matrix where d is the number of data dimensions and n the number of examples.
	:param labels: A 1 x n matrix with the label (actual value) for each data point.
	:param params: A dict, containing a key T, which is a positive integer number of steps to run
	:param hook: An optional hook function that is called in each iteration of the algorithm.
	:return:
	"""
	if params is None:
		params = {}
	T = params.get("T", 100)  # if T is not in params, default to 100
	(d, n) = data.shape

	theta = np.zeros((d, 1))

	for _ in range(T):
		found_separability = True
		for i in range(n):
			# TODO Best way to get single column of numpy array
			y_i = labels[:, i: i + 1]  # Get column
			X_i = data[:, i: i + 1]
			if y_i * (theta.T @ X_i) <= 0:
				theta += y_i * X_i
				found_separability = False
		if found_separability:
			return theta
	if hook is not None:
		hook(theta)
	return theta


def transform_polynomial_basis(x, order):
	"""
	Transform the data to a polynomial basis.

	:param x: A d x n matrix where d is the number of data dimensions and n the number of examples.
	:param order: The order of the polynomial basis to use.
	:return:
	"""

	x = np.concatenate((x, x[:, :-1] * x[:, 1:]), axis=1)


def start():
	X = np.array([[1 ,2, 4, 5], [2, 3, 5, 6], [3, 4, 6, 7], [4, 5, 7, 8], [5, 6, 8, 9]])
	y = np.array([[1, 1, 1, -1, -1]])
	transform_polynomial_basis(np.array([[2,3]]), 1)

if __name__ == "__main__":
	start()
