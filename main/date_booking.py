import config
from datetime import datetime

# Create a dictionary to store the bookings
bookings = {}

def check_availability(date):
    """Check the availability for the given date."""
    global booking
    if bookings[date]<=int(config.due):
        return (1)
    else:
        print(date,' date is already booked')

def add_booking(d):
    """Add a booking for the given date."""
    global bookings
    if d in bookings:
        
        if check_availability(d)==1:
            bookings[d] += 1
            print(d,'date booked')
    else:
        bookings[d] = 1
        

# Add a booking for today
'''n=0
while n<5:
    add_booking('2020-01-03')
    n+=1 '''
'''add_booking('2020-01-03')
add_booking('2020-01-04')
add_booking('2020-01-03')
add_booking('2020-01-03')
print(bookings)'''



# Check the availability for today
#print(check_availability(today))

# Check the availability for today again
#print(check_availability(today))




