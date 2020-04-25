from Life.AbstractLifeForm import AbstractLifeForm
from Life.Genetics.AbstractGene import AbstractGene


class Creature(AbstractLifeForm):
    base_gene_type = AbstractGene

    def __init__(self, genetic_makeup=None):
        genetic_makeup = genetic_makeup if genetic_makeup else self.base_gene_type()
        assert isinstance(genetic_makeup, self.base_gene_type)
        self.geneticMakeup = genetic_makeup

    def reproduce(self):
        return Creature(self._replicate_genetic_makeup())

    def _replicate_genetic_makeup(self):
        return self.geneticMakeup.replicate()
