from obj.rucksack import rucksack
from obj.item import item

##############
### PART 1 ###
##############

with open("input/test_input.txt") as file:
    lines = file.read()
    rucksack_pile = []
    for line in lines.split("\n"):
        rucksack_pile.append(rucksack(line))

priority_list = []
for each_rucksack in rucksack_pile:
    key = list(each_rucksack.find_common_item().items())[0][0]
    value = list(each_rucksack.find_common_item().items())[0][1]
    priority_list.append(value)

print(sum(priority_list))

##############
### PART 2 ###
##############

with open("input/real_data.txt") as file:
    lines = file.read()
    elf_triplicate = []
    elf_triplicate_items = []
    common_letters = []
    i = 1
    for line in lines.split("\n"):
        if i != 3:
            elf_triplicate.append(rucksack(line))
            i+=1
        else:
            elf_triplicate.append(rucksack(line))
            # now we have all 3 rucksack objects, lets get the common value
            for each_rucksack in elf_triplicate:
                inventory = each_rucksack.peek_total()   
                inventory_string =  []
                for each_item in inventory:
                    # this returns an item object, we need the letter
                    item_letter = each_item.return_item_letter()
                    # add the letter to a list
                    inventory_string.append(item_letter)
                    # add the list to a list (making a list of lists)
                elf_triplicate_items.append(inventory_string)
            # now we can iterate through the list of lists to get common letters
            # use list(set()) to remove duplicates, therefore we only get 1 output
            elf1, elf2, elf3 = elf_triplicate_items
            for item1 in list(set(elf1)):
                for item2 in list(set(elf2)):
                    if item1==item2:
                        for item3 in list(set(elf3)):
                            if item1==item3:
                                common_letters.append(item1)
                                break
                        break
            # now cleanup, and move onto the next triplicate
            elf_triplicate.clear()
            elf_triplicate_items.clear()
            i=1

# now we have a list of letters, we can convert these into items so that we can get their priorities
priorities = []
for letter in common_letters:
    new_item = item(letter)
    priority = new_item.return_item_priority()
    priorities.append(priority)

print(sum(priorities))