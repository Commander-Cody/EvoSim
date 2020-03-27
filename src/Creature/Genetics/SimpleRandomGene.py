from Creature.Genetics.AbstractGene import AbstractGene
from Util.RandomUtilities import flip_bit, get_random_positive_int, chance_allowed, get_bits


class SimpleRandomGene(AbstractGene):
    gene_size = 10
    default_mutation_chance = 0.3

    def __init__(self, value=None):
        """Generates a random integer with gene_size bits if no value is given"""
        self.value = value if value is not None else get_bits(self.gene_size)

    def replicate(self, mutation_chance=None):
        """Create a new gene with a mutation_chance to flip one bit"""
        if mutation_chance is None:
            mutation_chance = self.default_mutation_chance

        new_value = self.value
        if chance_allowed(mutation_chance):
            mutating_bit = get_random_positive_int(self.gene_size)
            new_value = flip_bit(self.value, mutating_bit)

        return SimpleRandomGene(new_value)

    def __eq__(self, other):
        if type(other) is type(self):
            return self.value == other.value
        return False
