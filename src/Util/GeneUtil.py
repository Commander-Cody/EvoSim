from random import SystemRandom

system_random = SystemRandom()


def flip_bit(value, bit_num):
    return value ^ (1 << bit_num)


def get_random_positive_int(upper_bound):
    return int(system_random.random() * upper_bound)


def chance_allowed(chance):
    return system_random.random() < chance


def get_bits(num):
    return system_random.getrandbits(num)
