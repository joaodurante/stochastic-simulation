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
    return result[0:5]

def get_tec(num):
    return (-numpy.log(num) * 15)

def get_ts(num):
    if num <= 0.6:
        return (-numpy.log(num) * 15)
    elif num > 0.6 and num <= 0.9:
        return ((-numpy.log(num) * 45) + 30)
    elif num > 0.9:
        return ((-numpy.log(num) * 180) + 60)

def get_arrival_time(last_row, tec):
    if last_row is not None:
        return last_row['arrival_time'] + tec
    else:
        return tec

def get_start_time(last_row, arrival_time):
    if last_row is not None:
        return max(last_row['end_time'], arrival_time)
    else:
        return arrival_time

def get_end_time(ts, start_time):
    return ts + start_time

def get_queue_time(arrival_time, start_time):
    return start_time - arrival_time

def get_system_time(ts, queue_time):
    return ts + queue_time

def get_free_time(last_row, arrival_time):
    if last_row is not None:
        diff = arrival_time - last_row['end_time']
        return max(0, diff)
    else:
        return arrival_time

def bank_queue(nums):
    rows = []

    for i in nums:
        last_row = rows[len(rows) - 1] if len(rows) > 0 else None

        tec = get_tec(i)
        ts = get_ts(i)
        arrival_time = get_arrival_time(last_row, tec)
        start_time = get_start_time(last_row, arrival_time)
        end_time = get_end_time(ts, start_time)
        queue_time = get_queue_time(arrival_time, start_time)
        system_time = get_system_time(ts, queue_time)
        free_time = get_free_time(last_row, arrival_time)
    

if __name__ == "__main__":
    a = 16807
    c = 0
    m = pow(2, 31) - 1
    init = 2
    n = 1000
    result = generate(a, m, n, init, c)
