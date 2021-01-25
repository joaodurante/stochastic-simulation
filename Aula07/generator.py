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
    t = 0
    x = 0
    y = 0
    i = 0

    rand1 = generate(16807, pow(2, 31) - 1, 5000, 2, 0)
    rand2 = generate(16807, pow(2, 31) - 1, 5000, 3, 0)
    print(rand1)
    print(rand2)

    while((x != 3 and y != 4) or t != 60):
        if i == 4999:
            rand1 = generate(16807, pow(2, 31) - 1, 5000, 2, 0)
            rand2 = generate(16807, pow(2, 31) - 1, 5000, 3, 1)
            i = 0

        if rand1[i] <= 0.3:
            t += 1

        if rand2[i] <= 0.35:
            x += 1
        elif 0.35 < rand2[i] and rand2[i] <= 0.8:
            y += 1
        elif 0.8 < rand2[i] and rand2[i] <= 0.9:
            x -= 1
        else:
            y -= 1
        
        t += 5
        i += 1

        # print("---")
        # print(x)
        # print(y)
        # print(t)

if __name__ == "__main__":
    drunk_simulator()