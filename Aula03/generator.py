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

def correlation_coefficient(x, y):
    n = len(x)
    summation_xy = sum([xi * yi for xi, yi in zip(x, y)])
    summation_x = sum(x)
    summation_y = sum(y)
    summation_xx = sum([xi ** 2 for xi in x])
    summation_yy = sum([yi ** 2 for yi in y])

    numerator = (n * summation_xy) - (summation_x * summation_y)

    first_denominator = math.sqrt(
        (n * summation_xx) - (summation_x ** 2)
    )

    second_denominator = math.sqrt(
        (n * summation_yy) - (summation_y ** 2)
    )

    return numerator / (first_denominator * second_denominator)

def chi_squared(x, y):
    summation = 0

    for xi, yi in zip(x, y):
        if yi != 0:
            res = ((xi - yi) ** 2) / yi
            summation += res

    return summation


if __name__ == "__main__":
    init = int(input('Insira o valor inicial: '))
    n = int(input('Insira o valor de n: '))

    # x = generate(45, 1024, n, init, 1)
    # y = generate(45, 1024, n, init+1, 1)
    # avg = average(x)
    # print('1-')
    # print('Media: {}, Desvio Padrão: {}'.format(avg, std_deviation(x, avg)))
    # print('Coeficiente de correlacao: {}'.format(correlation_coefficient(x, y)))
    # print('Qui-quadrado: {}'.format(chi_squared(x, y)))
    # plt.plot(x, y)
    # plt.show()

    # x = generate(45, 1024, n, init, 1)
    # y = generate(45, 1024, n, init+1, 1)
    # avg = average(x)
    # print('\n2-')
    # print('Media: {}, Desvio Padrão: {}'.format(avg, std_deviation(x, avg)))
    # print('Coeficiente de correlacao: {}'.format(correlation_coefficient(x, y)))
    # print('Qui-quadrado: {}'.format(chi_squared(x, y)))
    # plt.plot(x, y)
    # plt.show()

    # x = generate(383, 1000, n, init, 263)
    # y = generate(383, 1000, n, init+1, 263)
    # avg = average(x)
    # print('\n3-')
    # print('Media: {}, Desvio Padrão: {}'.format(avg, std_deviation(x, avg)))
    # print('Coeficiente de correlacao: {}'.format(correlation_coefficient(x, y)))
    # print('Qui-quadrado: {}'.format(chi_squared(x, y)))
    # plt.plot(x, y)
    # plt.show()

    # x = generate(97, 131072, n, init, 0)
    # y = generate(97, 131072, n, init+1, 0)
    # avg = average(x)
    # print('\n4-')
    # print('Media: {}, Desvio Padrão: {}'.format(avg, std_deviation(x, avg)))
    # print('Coeficiente de correlacao: {}'.format(correlation_coefficient(x, y)))
    # print('Qui-quadrado: {}'.format(chi_squared(x, y)))
    # plt.plot(x, y)
    # plt.show()

    x = generate(4, 9, 1000, 2, 1)
    y = generate(4, 9, 1000, 3, 1)
    print(x)
    print(y)
    avg = average(x)
    print('\n4-')
    print('Media: {}, Desvio Padrão: {}'.format(avg, std_deviation(x, avg)))
    print('Coeficiente de correlacao: {}'.format(correlation_coefficient(x, y)))
    print('Qui-quadrado: {}'.format(chi_squared(x, y)))
    plt.plot(x, y)
    plt.show()


