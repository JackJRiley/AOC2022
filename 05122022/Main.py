import re

# I can't begin to imagine how to parse the input, it is colwise instead of rowwise
# I'll manually convert it as the input isn't that big anyway
# But we can use regex for extracting the commands

##############
### Part 1 ###
##############

positions = []
with open("input/input.txt") as file:
    lines = file.read()
    for line in lines.split("\n"):
        stack = line.split(",")
        positions.append(stack)

commands_list = []
with open("input/commands.txt") as commands_file:
    commands = commands_file.read()
    for command in commands.split("\n"):
        command_regex = re.search("move (.+) from (.+) to (.+)", command)
        move_n = command_regex.group(1)
        move_from = command_regex.group(2)
        move_to = command_regex.group(3)
        command_array = [move_n, move_from, move_to]
        commands_list.append(command_array)

# Move everything according to the commands

for command in commands_list:
    n, take_from, add_to = command
    stack_from = positions[(int(take_from)-1)]
    stack_to = positions[(int(add_to)-1)]
    for i in range(int(n)):
        top_crate = stack_from.pop()
        stack_to.append(top_crate)

# Now read the ones at the top

top_crates = ""
for stack in positions:
    top_crate = stack.pop()
    top_crates+=top_crate

print(top_crates)

##############
### Part 2 ###
##############

positions = []
with open("input/input.txt") as file:
    lines = file.read()
    for line in lines.split("\n"):
        stack = line.split(",")
        positions.append(stack)

commands_list = []
with open("input/commands.txt") as commands_file:
    commands = commands_file.read()
    for command in commands.split("\n"):
        command_regex = re.search("move (.+) from (.+) to (.+)", command)
        move_n = command_regex.group(1)
        move_from = command_regex.group(2)
        move_to = command_regex.group(3)
        command_array = [move_n, move_from, move_to]
        commands_list.append(command_array)

# Move everything according to the commands, but this time save the top_crates to a list, then reverse it before EXTENDING (not appending)

for command in commands_list:
    n, take_from, add_to = command
    stack_from = positions[(int(take_from)-1)]
    stack_to = positions[(int(add_to)-1)]
    top_crates = []
    for i in range(int(n)):
        top_crate = stack_from.pop()
        top_crates.append(top_crate)
    top_crates.reverse()
    stack_to.extend(top_crates)

# Now read the ones at the top

print(positions)

top_crates = ""
for stack in positions:
    top_crate = stack.pop()
    top_crates+=top_crate

print(top_crates)