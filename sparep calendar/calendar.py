'''
here's my try at making a spaced repetition calendar

IMPORTANT - 
1. Date format is DDMMYYYY
	so the days need to be added as
	DDMMYYYY + (1000000)*N -> where n is the number of days till next revision
	the month needs to be added as

2. Appending to database, user inputs date and subject studied. 
	This date is modified first as the second third and fourth revision dates and then stored in the database( excel).

'''
"""
chap = input("Enter the name of the chapter studied today: ")
date_d = input("Enter the day studied on: ")
date_m = input("Enter the month studied on: ")
date_y = input("Enter the year studied on: ")


date3 = date + *1000000
date4 = date + 2*1000000

"""


import calendar
import datetime

print(calendar.Calendar(firstweekday=0))


