import math
import numpy
import matplotlib.pyplot as plt

def generate(a, m, n, init, c):
    result = []
    
    for _ in range(0, n):
        item = (a * init + c) % m
        result.append(item / m)
        init = item

    return result[0]

def drunk_simulator():
    t = 0
    x = 0
    y = 0
    init = 2


    while((x != 3 and y != 4) or t != 60):
        rand1 = generate(16807, pow(2, 31) - 1, init, 1000, 0)
        rand2 = generate(16807, pow(2, 31) - 1, init+2, 1000, 0)

        if rand1 <= 0.3:
            t += 1

        if rand2 <= 0.35:
            x += 1
        elif 0.35 < rand2 and rand2 <= 0.8:
            y += 1
        elif 0.8 < rand2 and rand2 <= 0.9:
            x += 1
        else:
            y -= 1
        
        t += 5

    print(x)
    print(y)
    print(t)

if __name__ == "__main__":
    drunk_simulator()