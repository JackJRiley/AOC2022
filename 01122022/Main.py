from obj.elf import elf 

# Part 1 - how much is being carried by the elf carrying the most

with open("inputs/real_data.txt") as file:
    lines = file.read()
    groups = lines.split("\n\n")
    #spawn elfs and give them their items
    elf_house = []
    for items in groups:
        new_elf = elf()
        for item in items.split("\n"):
            new_elf.take_to_inventory(item)
        elf_house.append(new_elf)

    #ask each elf in the elf house to count their inventory
    max = 0 
    for e in elf_house:
        answer = e.count_inventory()
        if answer > max:
            max = answer
        
    #what is the max?
    print(max)

# Part 2 - how much is being carried by the top 3 elves 

    # ask each elf how much they are carrying, but write it down
    answers = []
    for e in elf_house:
        answer = e.count_inventory()
        answers.append(answer)
    sorted_answers = sorted(answers, reverse=True)
    top3 = sum(sorted_answers[:3])
    print(top3)
