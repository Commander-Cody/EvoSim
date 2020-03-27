from Creature.Creature import Creature
from Creature.Genetics.SimpleRandomGene import SimpleRandomGene
from Environment.Simple2DEnvironment import Simple2DEnvironment
from Util.RandomUtilities import chance_allowed


class SimpleScenario:
    def _configure(self):
        SimpleRandomGene.default_mutation_chance = 0.1
        Creature.base_gene_type = SimpleRandomGene

    def __init__(self, creature_spawn_chance=0.1):
        self._configure()
        self.creature_spawn_chance = creature_spawn_chance
        self.environment = Simple2DEnvironment(100, 100)
        self.creatures = []

    def advance(self):
        self.environment.update()
        for area in self.environment.fuzzy_iter(10):
            if chance_allowed(self.creature_spawn_chance):
                self._create_creature(area.random_location(), Creature())

    def _create_creature(self, location, creature):
        self.creatures.append((location, creature))
