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


def normal_distribution(x, y):
    return

def poisson_distribution(x, y):
    return

def geometric_distribution(x, y):
    return

if __name__ == "__main__":
    a = 16807
    c = 0
    m = pow(2, 31) - 1
    init = int(input('Insira o valor inicial: '))
    n = int(input('Insira o valor de n: '))

    x = generate(a, m, n, init, c)
    y = generate(a, m, n, init+1, c)
    
    normal_distribution(x, y)
    poisson_distribution(x, y)
    geometric_distribution(x, y)
    

