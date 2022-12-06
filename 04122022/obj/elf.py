class elf:
    def __init__(self, range):
        self.range = range
        self.lower = self.range.split("-")[0]
        self.higher = self.range.split("-")[1]

    def return_lower(self):
        return int(self.lower)

    def return_higher(self):
        return int(self.higher)