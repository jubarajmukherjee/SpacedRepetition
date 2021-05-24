import calendar
import time
import datetime
days_added=[31,59,90,120,151,181,212,243,273,304,334]
import datetime

date=input("Enter date yyyy-mm-dd")

datee = datetime.datetime.strptime(date, "%Y-%m-%d")


month=datee.month
day= datee.day
year=datee.year
cultve_date=day

cultve_date=day+days_added[month-2]
print(cultve_date)
print(year)
first_notif= cultve_date+1
from datetime import datetime, date, timedelta

# initializing day number
day_num = first_notif

# print day number
print("The day number : " + str(day_num))
converted_num = str(day_num)
# adjusting day num
converted_num.rjust(3 + len(converted_num), '0')

# Initialize year
yr=year

# Initializing start date
strt_date = date(yr, 1, 1)

# converting to date
res_date = strt_date + timedelta(days=int(converted_num) - 1)
res = res_date.strftime("%m-%d-%Y")

# printing result
print("Resolved date : " + str(res))
