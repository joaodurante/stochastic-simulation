import numpy

def generate(a, m, n, init, c):
    result = []
    
    for _ in range(0, n):
        item = (a * init + c) % m
        result.append(item / m)
        init = item

    result.pop(0)
    return result


# f(x) = sin(x)cosh(x)
def calc_integer_a(x, y):
    count = 0
    total = len(x)

    for xi, yi in zip(x, y):
        fx = numpy.sin(xi) * numpy.cosh(xi)

        if yi < fx:
            count += 1
    
    return count / total

# f(x) = sin(x)sinh(x)
def calc_integer_b(x, y):
    count = 0
    total = len(x)

    for xi, yi in zip(x, y):
        fx = numpy.sin(xi) * numpy.sinh(xi)

        if yi < fx:
            count += 1
    
    return count / total


if __name__ == "__main__":
    a = 16807
    c = 0
    m = 1024
    init = 1
    n = int(input('Insira o valor de n: '))

    x = generate(a, m, n, init, c)
    y = generate(a, m, n, init+1, c)

    print(calc_integer_a(x, y))
    print(calc_integer_b(x, y))
