import numpy
import math

class Replica:
    def __init__(self, rows):
        self.rows = rows

        # QUEUE TIME
        self.queue_time_avg = self.calculate_avg('queue_time')
        self.queue_time_std_dev = self.calculate_std_dev('queue_time', self.queue_time_avg)

        # SYSTEM TIME
        self.system_time_avg = self.calculate_avg('system_time')
        self.system_time_std_dev = self.calculate_std_dev('system_time', self.system_time_avg)

        # SERVICE TIME
        self.service_time_avg = self.calculate_avg('service_time')
        self.service_time_std_dev = self.calculate_std_dev('service_time', self.service_time_avg)


    def calculate_avg(self, property):
        nums = [getattr(i, property) for i in self.rows]

        return sum(nums) / len(nums)

    def calculate_std_dev(self, property, avg):
        nums = [getattr(i, property) for i in self.rows]

        summation = sum([(x - avg) ** 2 for x in nums])
        return math.sqrt(summation) / (len(nums) - 1)

