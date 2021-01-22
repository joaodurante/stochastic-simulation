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


if __name__ == "__main__":
    a = 16807
    c = 0
    m = pow(2, 31) - 1
    # init = int(input('Insira o valor inicial: '))
    # n = int(input('Insira o valor de n: '))
    init = 2
    n = 1000

    x = generate(a, m, n, init, c)
    y = generate(a, m, n, init+1, c)
    