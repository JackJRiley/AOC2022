from .elf import elf

class elf_pair:
    def __init__(self, elf1, elf2):
        self.elf1 = elf1
        self.elf2 = elf2

    def ask_if_overlap_completely(self):
        elf1_values = list(range(self.elf1.return_lower(), self.elf1.return_higher()+1))
        elf1_length = len(elf1_values)
        elf2_values = list(range(self.elf2.return_lower(), self.elf2.return_higher()+1))
        elf2_length = len(elf2_values)
        
        intersection = list(set(elf1_values) & set(elf2_values))
        intersection_length = len(intersection)

        if(intersection_length==elf1_length or intersection_length==elf2_length):
            return True
        else:
            return False
        
    def ask_if_overlap_at_all(self):
        elf1_values = list(range(self.elf1.return_lower(), self.elf1.return_higher()+1))
        elf1_length = len(elf1_values)
        elf2_values = list(range(self.elf2.return_lower(), self.elf2.return_higher()+1))
        elf2_length = len(elf2_values)
        
        intersection = list(set(elf1_values) & set(elf2_values))
        intersection_length = len(intersection)

        if(intersection_length>=1):
            return True
        else:
            return False