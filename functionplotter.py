import numpy as np
import matplotlib.pyplot as plt


def plotter(data):
    plt.plot(data)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


def linear(a, b, max):
    data = [a*x + b for x in np.arange(max, step=1)]
    return data


def power(a, b, max):
    data = [x ** a + b for x in np.arange(max, step=1)]
    return data














