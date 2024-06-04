# The Range Middle

# Task 1

# print each day of the week only if the day is on an even index.

days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# print("Length of days_of_week")
# print(len(days_of_week))

for index in range(len(days_of_week)):
    if index % 2 == 0:
        print(index, days_of_week [index])

# Loop Condition Logic

# Task 1

#  write an infinite loop that asks the user a question until their answer triggers a break.

while True:
    user = input ("If Wednesday is on an even index, then keep going")
    if user == "exit":
        # even_days = False
        break

# Task 2

#  while loop that terminates after 5 iterations and print each iteration it is on.

days = []

days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

while len(days) < 5:
    print("Day of week:", days_of_week[len(days)], len(days))
    days.append( "day_of_week ")
print(days)