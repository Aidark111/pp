# Write a Python program to calculate two date difference in seconds.
from datetime import datetime

date1 = datetime(2024, 2, 15, 12, 0, 0)  # Sample date 1
date2 = datetime(2024, 2, 20, 12, 0, 0)  # Sample date 2

difference_in_seconds = (date2 - date1).total_seconds()

print("Difference in seconds:", difference_in_seconds)
