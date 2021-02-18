import math

class Utils:
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