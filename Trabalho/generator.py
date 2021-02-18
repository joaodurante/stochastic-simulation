import math
import numpy
from BankRow import BankRow
from Replica import Replica
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

# calculate average of averages
def calculate_avg_of_avgs(replicas):
    avgs = {}
    queue_sum = system_sum = service_sum = 0
    length = len(replicas)

    for i in replicas:
        queue_sum += i.queue_time_avg
        system_sum += i.system_time_avg
        service_sum += i.service_time_avg

    avgs['queue'] = queue_sum / length
    avgs['system'] = system_sum / length
    avgs['service'] = service_sum / length

    return avgs

# calculate standard deviation of avgs
def calculate_std_dev_of_avgs(replicas, queue_avg, system_avg, service_avg):
    std_devs = {}
    queue_summation = system_summation = service_summation = 0
    length = len(replicas)

    for i in replicas:
        queue_summation += (i.queue_time_avg - queue_avg) ** 2
        system_summation += (i.system_time_avg - system_avg) ** 2
        service_summation += (i.service_time_avg - service_avg) ** 2
    
    std_devs['queue'] = math.sqrt(queue_summation) / length
    std_devs['system'] = math.sqrt(system_summation) / length
    std_devs['service'] = math.sqrt(service_summation) / length

    return std_devs

# calculate confidence interval
def calculate_confidence_interval(avg, std_dev, t, alpha, n):
    lower_limit = avg - t * (std_dev / math.sqrt(n))
    upper_limit = avg + t * (std_dev / math.sqrt(n))

    return lower_limit, upper_limit

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

    avgs = calculate_avg_of_avgs(replicas)
    
    std_devs = calculate_std_dev_of_avgs(
        replicas,
        avgs['queue'],
        avgs['system'],
        avgs['service']
    )

    conf_interval['queue'] = calculate_confidence_interval(
        avgs['queue'],
        std_devs['queue'],
        STUDENT_T,
        ALPHA,
        NUMBER_OF_SEEDS
    )

    conf_interval['system'] = calculate_confidence_interval(
        avgs['system'],
        std_devs['system'],
        STUDENT_T,
        ALPHA,
        NUMBER_OF_SEEDS
    )

    conf_interval['service'] = calculate_confidence_interval(
        avgs['service'],
        std_devs['service'],
        STUDENT_T,
        ALPHA,
        NUMBER_OF_SEEDS
    )

    print(avgs)
    print(std_devs)
    print(conf_interval)