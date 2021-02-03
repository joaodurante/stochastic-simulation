import math
import numpy
from BankRow import BankRow
import matplotlib.pyplot as plt

def generate(a, m, n, init, c):
    result = []
    
    for _ in range(0, n):
        item = (a * init + c) % m
        result.append(item / m)
        init = item

    result.pop(0)
    return result[0:5]

def bank_queue(nums):
    rows = []

    for i in nums:
        last_row = rows[len(rows) - 1] if len(rows) > 0 else None
        row = BankRow(i, last_row)
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