import time


class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.filters_class = ("Mechanical", "Aragon", "Calcium")
        self.filters = {(x, self.filters_class[x - 1]): None for x in range(1, len(self.filters_class) + 1)}

    def add_filter(self, slot_num, filt):
        key = (slot_num, filt.__class__.__name__)
        if key in self.filters and not self.filters[key]:
            self.filters[key] = filt

    def remove_filter(self, slot_num):
        if isinstance(slot_num, int) and 1 <= slot_num <= 3:
            key = (slot_num, self.filters_class[slot_num - 1])
            if key in self.filters:
                self.filters[key] = None

    def get_filters(self):
        return tuple(self.filters.values())

    def water_on(self):
        return all(x is not None for x in self.filters.values()) and all(0 <= (time.time() - x.date) <= self.MAX_DATE_FILTER for x in self.filters.values())


class Filters:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if key == "date" and key in self.__dict__:
            return
        super().__setattr__(key, value)


class Mechanical(Filters):
    pass


class Aragon(Filters):
    pass


class Calcium(Filters):
    pass