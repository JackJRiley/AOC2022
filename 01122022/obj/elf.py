class elf: 
    def __init__(self, inventory=[]):
        self.inventory = []

    def take_to_inventory(self, item):
        self.inventory.append(item)

    def count_inventory(self):
        count=0
        for item in self.inventory:
            count+=int(item)
        return count
