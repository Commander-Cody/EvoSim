from Environment.Simple2DEnvironment import Simple2DEnvironment
from History.History import History
from Life.ProtoLifeform import ProtoLifeForm
from Util.RandomUtilities import chance_allowed


class PrimordialSoup:
    def __init__(self):
        self.history = History()
        self.environment = Simple2DEnvironment(100, 100)
        self.creatures = []

    def advance(self):
        self.history.log_time_advanced()

        self.environment.update()
        for area in self.environment.fuzzy_iter(10):
            creature = ProtoLifeForm.chance_create_new()
            if creature:
                loc = area.random_location()
                self.history.log_creature_created(creature, loc)
                self.creatures.append((loc, creature))

        for creature_info in self.creatures:
            if creature_info[1].chance_die():
                self.history.log_creature_died(creature_info[1], creature_info[0])
                self.creatures.remove(creature_info)

    def finish(self):
        self.history.print_summary()
