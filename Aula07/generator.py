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

def drunk_simulator():
    a = 2000
    m = pow(2, 12) - 1
    n = 10000
    init = 1
    c = 2

    t = 0
    x = 0
    y = 0
    i = 0

    rand1 = generate(a, m, n, init, c)
    rand2 = generate(a, m, n, init+1, c)

    while((x != 3 or y != 4) and t <= 360):
        if rand1[i] <= 0.3:
            t += 1

        if rand2[i] <= 0.35:
            x += 1
        elif 0.35 < rand2[i] and rand2[i] <= 0.8:
            y += 1
        elif 0.8 < rand2[i] and rand2[i] <= 0.9:
            x -= 1
        elif rand2[i] > 0.9:
            y -= 1
        
        t += 5
        i += 1

    print(x)
    print(y)
    print(t)

if __name__ == "__main__":
    drunk_simulator()