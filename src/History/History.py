"""Records everything happening at any given time. The history is a list where each entry contains the events
of the corresponding time, i.e. history[3] contains the events from t = 3"""


class History:
    events = ("CreatureCreatedEvents", "CreatureDeathEvents", "CreatureReplicatedEvents")

    def __init__(self):
        self.current_time = 0
        self.history = []
        self._initialize_current_log_entry()

    def log_time_advanced(self):
        self.current_time += 1
        self._initialize_current_log_entry()

    def log_creature_created(self, creature, position):
        self.current_events["CreatureCreatedEvents"].append({"creature": creature, "position": position})

    def log_creature_replicated(self, creature, position, new_creature):
        self.current_events["CreatureReplicatedEvents"].append({
            "creature": creature,
            "position": position,
            "new_creature": new_creature})

    def log_creature_died(self, creature, position):
        self.current_events["CreatureDeathEvents"].append({"creature": creature, "position": position})

    def print_summary(self):
        print("\nHistory summary:")
        for event_name in self.events:
            print(event_name, ": ", self._total_events_of_type(event_name))

    def _total_events_of_type(self, event_type):
        count = 0
        for entry in self.history:
            count += len(entry[event_type])
        return count

    def _initialize_current_log_entry(self):
        self.history.append(self._create_new_log_entry())
        self.current_events = self.history[self.current_time]

    @staticmethod
    def _create_new_log_entry():
        log_entry = {}
        for event_name in History.events:
            log_entry[event_name] = []
        return log_entry
