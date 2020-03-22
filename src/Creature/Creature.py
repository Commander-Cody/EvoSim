from Creature.Genetics.AbstractGene import AbstractGene


class Creature:
    gene_type = AbstractGene

    def __init__(self, genetic_makeup=None):
        assert isinstance(genetic_makeup, self.gene_type)
        self.geneticMakeup = genetic_makeup if genetic_makeup else self.gene_type()

    def reproduce(self):
        return Creature(self._replicate_genetic_makeup())

    def _replicate_genetic_makeup(self):
        return self.geneticMakeup.replicate()
