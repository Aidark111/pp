# Write a Python program to drop microseconds from datetime.


from datetime import datetime

current_date_time = datetime.now()
current_date_time_without_microseconds = current_date_time.replace(microsecond=0)

print("Current Date Time:", current_date_time)
print("Without Microseconds:", current_date_time_without_microseconds)
