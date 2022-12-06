from obj.elf import elf
from obj.elf_pair import elf_pair

elf_camp = []

with open("input/real_data.txt") as file:
    all_pairs = file.read()
    for pair in all_pairs.split("\n"):
        half_pair = pair.split(",")
        new_elf1 = elf(half_pair[0])
        new_elf2 = elf(half_pair[1])
        new_elf_pair = elf_pair(new_elf1, new_elf2)
        elf_camp.append(new_elf_pair)

##############
### Part 1 ###
##############

all_answers = []
for pair in elf_camp:
    answer = pair.ask_if_overlap_completely()
    all_answers.append(answer)

print(sum(all_answers))

##############
### Part 2 ###
##############

all_answers = []
for pair in elf_camp:
    answer = pair.ask_if_overlap_at_all()
    all_answers.append(answer)

print(sum(all_answers))