import string

class item:
    def __init__(self, item_letter):
        self.item_letter = item_letter

        alphaALPHA = string.ascii_lowercase + string.ascii_uppercase
        nums = list(range(1,53))
        map_dict = {alphaALPHA[i]:nums[i] for i in range(len(nums))}

        self.item_priority = map_dict[item_letter]

    def return_item_letter(self):
        return self.item_letter

    def return_item_priority(self):
        return self.item_priority