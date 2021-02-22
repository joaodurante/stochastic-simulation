from constants import *
from BankRow import BankRow
from Replica import Replica
from Utils import Utils
from random import seed, randint

if __name__ == "__main__":
    seed(1)
    used_seeds = []
    replicas = []
    conf_interval = {}

    for i in range(0, NUMBER_OF_SEEDS):
        seed = Utils.generate_seed(used_seeds)
        used_seeds.append(seed)
        result = Utils.generate(A, M, N, seed, C)
        replicas.append(Replica(result))

    avgs = Utils.calculate_avg_of_avgs(replicas)
    
    std_devs = Utils.calculate_std_dev_of_avgs(
        replicas,
        avgs['queue'],
        avgs['system'],
        avgs['service']
    )

    conf_interval['queue'] = Utils.calculate_confidence_interval(
        avgs['queue'],
        std_devs['queue'],
        STUDENT_T,
        ALPHA,
        NUMBER_OF_SEEDS
    )

    conf_interval['system'] = Utils.calculate_confidence_interval(
        avgs['system'],
        std_devs['system'],
        STUDENT_T,
        ALPHA,
        NUMBER_OF_SEEDS
    )

    conf_interval['service'] = Utils.calculate_confidence_interval(
        avgs['service'],
        std_devs['service'],
        STUDENT_T,
        ALPHA,
        NUMBER_OF_SEEDS
    )
    print('NUMBERS OF REPLICA: {}'.format(len(replicas)))
    print('\n--- AVERAGE ---')
    print(avgs)
    print('\n--- STANDARD DEVIATION ---')
    print(std_devs)
    print('\n--- CONFIDENCE INTERVAL ---')
    print(conf_interval)