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
    # constants 
    TIME_TARGET = 60

    # generator values
    a = 16807
    m = pow(2, 31) - 1
    n = 100000
    init = 2
    c = 0

    # temp values
    t = 0
    x = 0
    y = 0
    i = 0

    # random values
    rand1 = generate(a, m, n, init, c)
    rand2 = generate(a, m, n, init+1, c)

    # final values
    result = []
    filtered_result = []

    while(i < len(rand1)):
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

        if((x == 3 and y == 4) or t >= TIME_TARGET):
            result.append({'x': x, 'y': y, 't': t})
            t = 0
            x = 0
            y = 0

    # filter unique time values
    for i in result:
        if i['x'] == 3 and i['y'] == 4 and i['t'] <= TIME_TARGET and i not in filtered_result:
            filtered_result.append(i)

    # print final results
    print([i['t'] for i in filtered_result])
    print(len(filtered_result))
    print(len(result))
    

if __name__ == "__main__":
    drunk_simulator()