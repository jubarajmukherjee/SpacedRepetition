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



#first notification


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
print(res_date)

#second notification



second_notif=cultve_date+7

conv_num=str(second_notif)
print(conv_num)
conv_num.rjust(3+len(conv_num),'0')
rest_date=strt_date+timedelta(days=int(conv_num)-1)
rest=rest_date.strftime("%m-%d-%y")
print(rest)

#third notification
third_notif=cultve_date+31
con_num=str(third_notif)
print(third_notif)
con_num.rjust(3+len(con_num),'0')
r_date=strt_date+timedelta(days=int(con_num)-1)
r=r_date.strftime("%m-%d-%y")
print(r)