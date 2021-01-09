import math
import numpy
import matplotlib.pyplot as plt

def generate(a, m, n, init, c):
    result = []
    
    for _ in range(0, n):
        item = (a * init + c) % m
        result.append(item / m)
        init = item

    result.pop(0)
    return result


def uniform_method(nums, a, b):
    sequence = []

    for i in nums:
        # temp = (b - a) * i + a
        temp = 1 - (b - a)
        sequence.append(temp)

    return sequence

def exponential_method(nums, alpha, x):
    sequence = []

    for i in nums:
        # temp = -(numpy.log(i) / alpha)
        temp = alpha * numpy.exp(- alpha * i)
        sequence.append(temp)
    
    return sequence

def weibull_method(nums, alpha, beta):
    sequence = []

    for i in nums:
        temp = alpha * (beta ** -alpha) * (i ** (alpha - 1)) * (numpy.exp(-(i / beta) ** alpha))
        sequence.append(temp)

    return sequence

def erlang_method(nums, alpha, k):
    sequence = []

    for i in nums:
        temp = (alpha * (numpy.exp(-alpha * i)) * (alpha * i) ** (k - 1)) / math.factorial(k - 1)
        sequence.append(temp)

    return sequence


if __name__ == "__main__":
    a = 16807
    c = 0
    m = pow(2, 31) - 1
    init = int(input('Insira o valor inicial: '))
    n = int(input('Insira o valor de n: '))

    x = generate(a, m, n, init, c)
    
    uniform = uniform_method(x, 5, 10)
    plt.plot(uniform)
    plt.show()

    exponential = exponential_method(x, 5, 2)
    plt.plot(exponential)
    plt.show()

    weibull = weibull_method(x, 2, 1)
    plt.plot(weibull)
    plt.show()

    erlang = erlang_method(x, 2, 3)
    plt.plot(erlang)
    plt.show()

