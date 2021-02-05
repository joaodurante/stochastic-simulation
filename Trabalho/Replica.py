import numpy

class Replica:
    def __init__(self, rows):
        self.rows = rows

        # QUEUE TIME
        self.queue_time_avg = self.calculate_avg('queue_time')
        self.queue_time_std_dev = self.calculate_std_dev('queue_time')

        # SYSTEM TIME
        self.system_time_avg = self.calculate_avg('system_time')
        self.system_time_std_dev = self.calculate_std_dev('system_time')

        # SERVICE TIME
        self.service_time_avg = self.calculate_avg('service_time')
        self.service_time_std_dev = self.calculate_std_dev('service_time')


    def calculate_avg(self, property):
        return 1

    def calculate_std_dev(self, property):
        return 2

