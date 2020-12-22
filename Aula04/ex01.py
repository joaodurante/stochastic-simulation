def generate(a, m, n, init, c):
    result = []
    
    for _ in range(0, n):
        item = (a * init + c) % m
        result.append(item / m)
        init = item

    result.pop(0)
    return result


def calc_pi(x, y):
    p_intern = 0
    p_square = 0
    for i, j in zip(x,y):
        d = i ** 2 + j ** 2
        if d <= 1:
            p_intern += 1
        p_square += 1
    
    return 4 * (p_intern / p_square)

if __name__ == "__main__":
    a = 16807
    c = 0
    m = 1024
    init = 2
    n = int(input('Insira o valor de n: '))

    x = generate(a, m, n, init, c)
    y = generate(a, m, n, init+1, c)

    print(calc_pi(x, y))
