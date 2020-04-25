"""
A proto creature that can spawn randomly from the primordial ooze and has a chance to replicate
"""
from Life.Genetics.SimpleRandomGene import SimpleRandomGene
from Util.RandomUtilities import chance_allowed


class ProtoLifeForm:
    formation_chance = 0.01
    death_chance = 0.1

    @staticmethod
    def chance_create_new():
        if chance_allowed(ProtoLifeForm.formation_chance):
            return ProtoLifeForm()

    def __init__(self, replication_chance=0.001, genes=None):
        self.replication_chance = replication_chance
        if genes is None:
            self.genes = SimpleRandomGene()
        else:
            self.genes = genes.replicate()

    def chance_die(self):
        if chance_allowed(self.death_chance):
            return True
        return False

    def chance_replicate(self):
        if chance_allowed(self.replication_chance):
            return ProtoLifeForm(self.replication_chance, self.genes)
