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

def average(nums):
    return sum(nums) / len(nums)
        

def std_deviation(nums, avg):
    summation = sum([(x - avg) ** 2 for x in nums])
    return math.sqrt(summation) / (len(nums) - 1)

def normal_distribution(x, y):
    seq = []
    for xi, yi in zip(x, y):
        temp = math.sqrt(-2 * numpy.log(xi)) * numpy.cos(2 * numpy.pi * yi)
        seq.append(temp)
    
    plt.plot(seq)
    plt.show()


def poisson_distribution(nums, lambda_value):
    B = math.exp(-lambda_value)
    x = 0
    P = 1
    res = []

    for i in nums:
        P *= i
        if P < B:
            res.append(x)
            x = 0
            P = 1
        else:
            x += 1

    print(res)
    plt.plot(res)
    plt.show()
    

def geometric_distribution(nums, p):
    x = []
    y = []
    q = 1 - p

    for i in nums:
        tempx = 1 + (numpy.log(i) / numpy.log(1 - p))
        x.append(tempx)

        tempy = 1 - q ** (tempx + 1)
        y.append(tempy)

    plt.plot(x,y)
    plt.show()

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
    
    normal_distribution(x, y)
    poisson_distribution(x, 1)
    geometric_distribution(x, 0.2)