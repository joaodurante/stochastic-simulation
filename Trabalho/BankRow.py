import numpy

class BankRow:
    """
        A single row of a bank report

        Attributes:
            random: the random value that will be used to calculate the properties
            last_row: the last BankRow (if it's the first one it receive 'None')
    """
    def __init__(self, random, last_row):
        self.last_row = last_row
        self.tec = self.get_tec(random)
        self.ts = self.get_ts(random)
        self.arrival_time = self.get_arrival_time()
        self.start_time = self.get_start_time()
        self.end_time = self.get_end_time()
        self.queue_time = self.get_queue_time()
        self.system_time = self.get_system_time()
        self.free_time = self.get_free_time()
        self.service_time = self.get_service_time()

    def get_tec(self, num):
        return (-numpy.log(num) * 15)

    def get_ts(self, num):
        if num <= 0.6:
            return ((-numpy.log(num) * 15) + 15)
        elif num > 0.6 and num <= 0.9:
            return ((-numpy.log(num) * 45) + 30)
        elif num > 0.9:
            return ((-numpy.log(num) * 180) + 60)

    def get_arrival_time(self):
        if self.last_row is not None:
            return self.last_row.arrival_time + self.tec
        else:
            return self.tec

    def get_start_time(self):
        if self.last_row is not None:
            return max(self.last_row.end_time, self.arrival_time)
        else:
            return self.arrival_time

    def get_end_time(self):
        return self.ts + self.start_time

    def get_queue_time(self):
        return self.start_time - self.arrival_time

    def get_system_time(self):
        return self.ts + self.queue_time

    def get_free_time(self):
        if self.last_row is not None:
            diff = self.arrival_time - self.last_row.end_time
            return max(0, diff)
        else:
            return self.arrival_time
    
    def get_service_time(self):
        return self.end_time - self.start_time

    def to_string(self):
        return 'TEC: {}, TS: {}, ARRIVAL_TIME: {}, START_TIME: {}, END_TIME: {}, QUEUE_TIME: {}, SYSTEM_TIME: {}, FREE_TIME: {}' \
            .format(self.tec, self.ts, self.arrival_time, self.start_time, self.end_time, self.queue_time, self.system_time, self.free_time)

