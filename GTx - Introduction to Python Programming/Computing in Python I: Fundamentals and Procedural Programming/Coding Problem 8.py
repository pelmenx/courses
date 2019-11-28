current_hour = 8
current_minute = 48
current_section = "PM"
due_hour = 5
due_minute = 15
due_section = "PM"

# False
# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Given the current time and deadline time represented by the
# variables above, determine if an assignment is still eligible
# for submission. An assignment is eligible if the time
# represented by current_hour, current_minute, and
# current_section is before the time represented by due_hour,
# due_minute, and due_section.

# Add your code here!
if current_hour == 12:
    current_hour -= 12
if due_hour == 12:
    due_hour -= 12

if (current_section < due_section):
    print(True)
elif ((current_section <= due_section) and (current_hour < due_hour)):
    print(True)
elif ((current_section <= due_section) and (current_hour < due_hour) and (current_minute < due_minute)):
    print(True)
else:
    print(False)
