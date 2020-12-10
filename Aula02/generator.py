import math
import numpy

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

# def std_deviation(nums):
#     first = 1 / (len(nums) - 1)
#     sec = sum([x ** 2 for x in nums])
#     third = (sum(nums) ** 2) / len(nums)
#     prod = first * (sec - third)

#     if prod >= 0:
#         return math.sqrt(prod)

def correlation_coefficient(x, y):
    n = len(x)
    summation_xy = sum([xi * yi for xi, yi in zip(x, y)])
    summation_x = sum(x)
    summation_y = sum(y)
    summation_xx = sum([xi ** 2 for xi in x])
    summation_yy = sum([yi ** 2 for yi in y])

    numerator = (n * summation_xy) - (summation_x * summation_y)
    denominator = math.sqrt(
        (n * summation_xx) - \
        ((summation_x ** 2) * math.sqrt((n * summation_yy) - (summation_y ** 2)))
    )

    return numerator / denominator

def chi_squared(x, y):
    summation = 0

    for xi, yi in zip(x, y):
        res = ((xi - yi) ** 2) / yi
        summation += res

    return summation


if __name__ == "__main__":
    a = 16807
    c = 0
    m = pow(2, 31) - 1
    init = int(input('Insira o valor inicial: '))
    n = int(input('Insira o valor de n: '))

    x = generate(a, m, n, init, c)
    y = generate(a, m, n, init+1, c)
    
    avg = average(x)
    std = std_deviation(x, avg)
    corr = correlation_coefficient(x, y)
    chi = chi_squared(x, y)

    print(x)
    print(avg)
    print(std)
    print(corr)
    print(chi)

