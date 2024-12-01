# Reading the file, and creating the two lists

f = open("day1/input.txt", "r")

l1 = []
l2 = []

for line in f:
    parts = line.split("   ")
    l1.append(parts[0])
    l2.append(parts[1])

###########################   PART 1   #######################################

l1.sort()
l2.sort()

# I've allowed myself list comprehensions at the very least =P
differences = [abs(int(item1) - int(item2)) for item1, item2 in zip(l1, l2)]

print("Answer (Part 1): " + str(sum(differences)))

###########################   PART 2   #######################################

occurances = {}

# Find which numbers occur in list 1
for i in l1:
    if int(i) not in occurances:
        occurances.update({int(i): 0})

# Increment the dictionary value (which can be seen as a "counter") for the
# corresponding number in list 2
for i in l2:
    if int(i) in occurances:
        # print(occurances[int(i)])
        occurances[int(i)] = occurances.get(int(i)) + 1

result = 0

# Calculate and sum up the similarity scores
for i in l1:
    result += int(i) * occurances[int(i)]

print("Answer (Part 2): " + str(result))

# File IO cleanup
f.close()