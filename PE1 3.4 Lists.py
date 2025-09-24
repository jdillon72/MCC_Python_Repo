# Varialbes of lists for assignment.

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
steps = []

# For loop for days in the week. 

for day in days:
    steps_input = input("How many steps did you take on " + day + '?: ')
    steps_int = int(steps_input)
    steps.append(steps_int)

# Print statements for display results and then average steps taken that day.

step_total = sum(steps)

print()
print('Total steps: ' + str(step_total))
print('Average steps: ' + str(step_total//7))