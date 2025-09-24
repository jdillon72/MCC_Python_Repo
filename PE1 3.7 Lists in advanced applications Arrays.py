# Time of Day Variable & list.

times_slots = ["Morning", "Midday", "Afternoon", "Evening"] 

heart_bpm = 0 # Total heart rate BPM.

heart_rates = []

# For loop to retrieve info from user.
for time_slot in times_slots:
    heart_rate = int(input(f"Please enter the heart rate (in BPM) the {time_slot}: "))
    heart_rates.append([time_slot, heart_rate])
    
# For loop for taking average BPM in time of day.
total_heart_rate = 0
for data in heart_rates:
    total_heart_rate += data[1] # "data[1]" is the input heart rate.
average_heart_rate = total_heart_rate / len(heart_rates)
print(f"Average heart rate today: {average_heart_rate:.2f} BPM")
