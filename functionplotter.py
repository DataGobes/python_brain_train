import numpy as np
import matplotlib.pyplot as plt


def plotter(data, start, stop):
    x = np.arange(start=start, stop=stop, step=1)
    plt.plot(x, data)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


def linear(a, b, start, stop):
    """

    :param a: linear coefficient
    :param b: constant
    :param start: minimum x value
    :param stop: maximum x value
    """
    data = [a*x + b for x in np.arange(start=start, stop=stop, step=1)]
    start = start
    stop = stop
    plotter(data, start, stop)


def power(a, b, start, stop):
    """

    :param a: function order
    :param b: constant
    :param start: minimum x value
    :param stop: maximum x value
    """
    data = [x ** a + b for x in np.arange(start=start, stop=stop, step=1)]
    start = start
    stop = stop
    plotter(data, start, stop)




















