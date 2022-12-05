from .item import item

class rucksack:
    def __init__(self, item_string):
        self.item_string = item_string
        self.compartment1 = []
        self.compartment2 = []

        length = len(self.item_string)
        for letter in self.item_string[:int(length/2)]:
            self.compartment1.append(item(letter))

        for letter in self.item_string[int(length/2):length]:
            self.compartment2.append(item(letter))

        self.total = self.compartment1 + self.compartment2

    def peek_compartment1(self):
        return self.compartment1

    def peek_compartment2(self):
        return self.compartment2

    def peek_total(self):
        return self.total

    def find_common_item(self):
        for itemObj1 in self.compartment1:
            item_letter1 = itemObj1.return_item_letter()
            for itemObj2 in self.compartment2:
                item_letter2 = itemObj2.return_item_letter()
                if(item_letter1 == item_letter2):
                    return {itemObj1.return_item_letter():itemObj1.return_item_priority()}
                    break