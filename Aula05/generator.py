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
    x = []
    y = []

    for i in nums:
        # x
        temp = (b - a) * i + a
        x.append(temp)
        
        # y
        if a <= temp and temp <= b:
            temp = 1 - (b - a)
            y.append(temp)
        else:
            x.pop(-1)

    plt.plot(x, y)
    plt.show()

def exponential_method(nums, alpha):
    x = []
    y = []

    for i in nums:
        # x
        temp = -(numpy.log(i) / alpha)
        x.append(temp)

        # y
        temp = alpha * numpy.exp(- alpha * temp)
        y.append(temp)
    
    plt.plot(x, y)
    plt.show()

def weibull_method(nums, alpha, beta):
    x = []
    y = []

    for i in nums:
        # temp = beta * (-(numpy.log(i) ** (1 / alpha)))
        # x.append(temp)

        temp = alpha * (beta ** -alpha) * (i ** (alpha - 1)) * (numpy.exp(-(i / beta) ** alpha))
        y.append(temp)

    plt.plot(nums, y)
    plt.show()

def erlang_method(nums, k, alpha):
    x = []
    y = []

    for i in nums:
        # x    
        temp = (- numpy.log(i)) / alpha
        x.append(temp)

        # y
        temp = (alpha * (numpy.exp(-alpha * temp)) * (alpha * temp) ** (k - 1)) / math.factorial(k - 1)
        y.append(temp)

    plt.plot(x,y)
    plt.show()


if __name__ == "__main__":
    a = 16807
    c = 0
    m = pow(2, 31) - 1
    init = int(input('Insira o valor inicial: '))
    n = int(input('Insira o valor de n: '))

    x = generate(a, m, n, init, c)
    
    uniform_method(x, 5, 10)
    exponential_method(x, 2)
    weibull_method(x, 1, 0.5)
    erlang_method(x, 3, 1)

