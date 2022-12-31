#this file is to suggest alternatve dates for lecturers those who didn't get their prefered dates
import calendar
from datetime import datetime, timedelta

# Specify the year and month

year = 2022
month = 12 

# Get the number of days in the month
num_days = calendar.monthrange(year, month)[1]

# Create a list of dates for the month
dates = [datetime(year, month, day) for day in range(1, num_days+1)]

# Print the dates
for date in dates:
    print(date.strftime('%Y-%m-%d'))
