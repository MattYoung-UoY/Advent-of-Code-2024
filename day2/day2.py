
f = open("day2/input.txt", "r")

reports = []
for line in f:
    reports.append(line.removesuffix("\n").split(" "))

# Converts all the strings to ints
reports = [[int(x) for x in report] for report in reports]

######################### PART 1 ############################

num_safe = 0

for report in reports:
    gradients = []
    for i in range(len(report)-1):
        gradients.append(report[i] - report[i+1])
    if gradients[0] < 0:
        gradients = [x*-1 for x in gradients]
    
    safe_report = True

    for gradient in gradients:
        if gradient <= 0 or gradient > 3:
            safe_report = False
            break

    if safe_report:
        num_safe += 1
    
print("Answer (Part 1): " + str(num_safe))

######################### PART 2 ############################

num_safe_pt2 = 0

def is_safe_report(report):
    gradients = []
    for i in range(len(report)-1):
        gradients.append(report[i] - report[i+1])
    if gradients[0] < 0:
        gradients = [x*-1 for x in gradients]

    for gradient in gradients:
        if gradient <= 0 or gradient > 3:
            return False
        
    return True


for report in reports:
    gradients = []
    for i in range(len(report)-1):
        gradients.append(report[i] - report[i+1])
    if gradients[0] < 0:
        gradients = [x*-1 for x in gradients]
    
    safe_report = True

    for i in range(len(gradients)):
        if gradients[i] <= 0 or gradients[i] > 3:
            modified_report = [report[i-1]] + report[i+1:]
            safe_report = is_safe_report(modified_report)
            if not safe_report:
                safe_report = False
                break

    if safe_report:
        num_safe_pt2 += 1
    
print("Answer (Part 2): " + str(num_safe_pt2))

# File IO Cleanup
f.close()