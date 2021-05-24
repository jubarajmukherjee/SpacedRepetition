import calendar
import time
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


