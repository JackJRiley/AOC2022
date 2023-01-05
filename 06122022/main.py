with open("inputs/real_input.txt") as file:
    input = file.read()
print(input)
length = len(input)

##############
### PART 1 ###
##############

four_mers = []
for i in range(length-3):
    four_mers.append(input[i:(i+4)])

i=1
all_counts = []
for four_mer in four_mers:
    i+=1
    four_mer_counts = 0
    for letter in four_mer:
        counts = four_mer.count(letter)
        four_mer_counts += counts
    all_counts.append(four_mer_counts)


i=0
for count in all_counts:
    i+=1
    if(count==4):
        break

#adjust for 4mer
i=i+3
print(i)

##############
### PART 2 ###
##############

fourteen_mers = []
for i in range(length-13):
    fourteen_mers.append(input[i:(i+14)])

i=1
all_counts = []
for fourteen_mer in fourteen_mers:
    i+=1
    fourteen_mer_counts = 0
    for letter in fourteen_mer:
        counts = fourteen_mer.count(letter)
        fourteen_mer_counts += counts
    all_counts.append(fourteen_mer_counts)


i=0
for count in all_counts:
    i+=1
    if(count==14):
        break

#adjust for 14mer
i=i+13
print(i)