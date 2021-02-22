import math
from random import seed, randint

class Utils:
    """
        Class that contains useful methods
    """
    @staticmethod
    def generate(a, m, n, init, c):
        """
            Generates pseudo random numbers

            Parameters:
                a: integer number between 1 and m
                m: prime number
                n: number of iterations
                init: initial value
                c: increment ( c=0 -> congruential method, c != 0 -> mixed congruential method)
        """
        result = []
        
        for _ in range(0, n):
            item = (a * init + c) % m
            result.append(item / m)
            init = item

        result.pop(0)
        return result

    @staticmethod
    def calculate_avg_of_avgs(replicas):
        """
            Calculate average of averages

            Parameters:
                replicas: list of Replicas
            
            Returns:
                dict: Dictionary containing avgs of queue, system and service
        """
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

    @staticmethod
    def calculate_std_dev_of_avgs(replicas, queue_avg, system_avg, service_avg):
        """
            Calculate standard deviation of avgs
        """

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

    @staticmethod
    def calculate_confidence_interval(avg, std_dev, t, alpha, n):
        """
            Calculate confidence interval
            Parameters:
                avg: average
                std_dev: standard deviation
                t: student's t value
                alpha: alpha value
                n: number of replicas
        """
        lower_limit = avg - t * (std_dev / math.sqrt(n))
        upper_limit = avg + t * (std_dev / math.sqrt(n))

        return lower_limit, upper_limit

    @staticmethod
    def generate_seed(seeds):
        """
            Generate a new random seed
            Parameters:
                seeds: array containing the used seeds
            
            Returns:
                int: generated seed
        """
        seed = randint(0, 500)

        while seed in seeds:
            seed = randint(0, 500)

        seeds.append(seed)
        return seed