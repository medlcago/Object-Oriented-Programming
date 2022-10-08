class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.__things = []

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing: Thing):
        if self.get_total_weight() + thing.weight <= self.max_weight:
            self.things.append(thing)

    def remove_thing(self, index):
        self.things.pop(index)

    def get_total_weight(self):
        return sum(x.weight for x in self.things)