import math
import numpy
from BankRow import BankRow
from Replica import Replica
import matplotlib.pyplot as plt
from random import seed, randint

# constants
OPENING_TIME = 0
CLOSING_TIME = 30
seed(1)

def generate(a, m, n, init, c):
    result = []
    
    for _ in range(0, n):
        item = (a * init + c) % m
        result.append(item / m)
        init = item

    result.pop(0)
    return result

def is_the_bank_open(arrival_time):
    if arrival_time >= OPENING_TIME and arrival_time <= CLOSING_TIME:
        return True
    else:
        return False

def bank_queue(nums):
    rows = []

    for i in nums:
        last_row = rows[len(rows) - 1] if len(rows) > 0 else None
        row = BankRow(i, last_row)

        # check if the arrival_time is inside interval
        if is_the_bank_open(row.arrival_time):
            rows.append(row)
            row.print_properties()

    return rows
    
def generate_seed(seeds):
    seed = randint(0, 500)

    while seed in seeds:
        seed = randint(0, 500)

    seeds.append(seed)
    return seed

if __name__ == "__main__":
    a = 16807
    c = 0
    m = pow(2, 31) - 1
    n = 1000
    used_seeds = []
    replicas = []

    for i in range(0, 120):
        seed = generate_seed(used_seeds)
        result = generate(a, m, n, seed, c)
        rows = bank_queue(result)
        replicas.append(Replica(rows))

    