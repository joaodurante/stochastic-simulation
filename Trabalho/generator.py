import math
import numpy
from BankRow import BankRow
from Replica import Replica
from Utils import Utils
import matplotlib.pyplot as plt
from random import seed, randint

# CONSTANTS
OPENING_TIME = 0
CLOSING_TIME = 30
NUMBER_OF_SEEDS = 121
ALPHA = 0.05
STUDENT_T = 1.96
seed(1)

# generate pseudo random numbers
def generate(a, m, n, init, c):
    result = []
    
    for _ in range(0, n):
        item = (a * init + c) % m
        result.append(item / m)
        init = item

    result.pop(0)
    return result

# check if the arrival_time is inside of opening hours
def is_the_bank_open(arrival_time):
    if arrival_time >= OPENING_TIME and arrival_time <= CLOSING_TIME:
        return True
    else:
        return False

# generate bank system
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

# generate seeds
def generate_seed(seeds):
    seed = randint(0, 500)

    while seed in seeds:
        seed = randint(0, 500)

    seeds.append(seed)
    return seed

# main
if __name__ == "__main__":
    a = 16807
    c = 0
    m = pow(2, 31) - 1
    n = 1000
    used_seeds = []
    replicas = []
    conf_interval = {}

    for i in range(1, NUMBER_OF_SEEDS):
        seed = generate_seed(used_seeds)
        result = generate(a, m, n, seed, c)
        rows = bank_queue(result)
        replicas.append(Replica(rows))

    avgs = Utils.calculate_avg_of_avgs(replicas)
    
    std_devs = Utils.calculate_std_dev_of_avgs(
        replicas,
        avgs['queue'],
        avgs['system'],
        avgs['service']
    )

    conf_interval['queue'] = Utils.calculate_confidence_interval(
        avgs['queue'],
        std_devs['queue'],
        STUDENT_T,
        ALPHA,
        NUMBER_OF_SEEDS
    )

    conf_interval['system'] = Utils.calculate_confidence_interval(
        avgs['system'],
        std_devs['system'],
        STUDENT_T,
        ALPHA,
        NUMBER_OF_SEEDS
    )

    conf_interval['service'] = Utils.calculate_confidence_interval(
        avgs['service'],
        std_devs['service'],
        STUDENT_T,
        ALPHA,
        NUMBER_OF_SEEDS
    )

    print(avgs)
    print(std_devs)
    print(conf_interval)