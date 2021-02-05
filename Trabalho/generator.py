import math
import numpy
from BankRow import BankRow
import matplotlib.pyplot as plt

# constants
OPENING_TIME = 0
CLOSING_TIME = 30

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
    

if __name__ == "__main__":
    a = 16807
    c = 0
    m = pow(2, 31) - 1
    init = 2
    n = 1000
    result = generate(a, m, n, init, c)
    rows = bank_queue(result)