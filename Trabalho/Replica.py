import numpy
import math
from constants import *
from BankRow import BankRow

class Replica:
    """
        A replica of a bank queue report

        Attributes:
            pseudo_rand_list: list containing pseudo random numbers 
    """
    def __init__(self, pseudo_rand_list):

        self.rows = self.generate_bank_queue(pseudo_rand_list)

        # QUEUE TIME
        self.queue_time_avg = self.calculate_avg('queue_time')

        # SYSTEM TIME
        self.system_time_avg = self.calculate_avg('system_time')

        # SERVICE TIME
        self.service_time_avg = self.calculate_avg('service_time')


    def generate_bank_queue(self, nums):
        """
            Generates a bank queue

            Parameters:
                nums: list containing values that will be used to calculate BankRow

            Returns:
                list: list of generated BankRow
        """

        rows = []
        for i in nums:
            last_row = rows[len(rows) - 1] if len(rows) > 0 else None
            row = BankRow(i, last_row)

            # check if the arrival_time is inside interval
            if self.is_the_bank_open(row.arrival_time):
                rows.append(row)

        return rows

    def is_the_bank_open(self, arrival_time):
        """
            Check if the arrival_time is inside of opening hours

            Parameters:
                arrival_time: customer arrival time at bank

            Returns:
                bool: indicates if arrival time is inside bank opening hours
        """

        if arrival_time >= OPENING_TIME and arrival_time <= CLOSING_TIME:
            return True
        else:
            return False

    def calculate_avg(self, property):
        """
            Calculate average of property received

            Parameters:
                property: property name
            
            Returns:
                float: average calculated
        """

        nums = [getattr(i, property) for i in self.rows]
        return sum(nums) / len(nums)
