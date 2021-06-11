import datetime
import sqlite3
import plyer


##########################
### REQUIRED FUNCTIONS ###
##########################

#CHECK LAST EXISTING ROW

def checkLastRow():
    lastRowCommand = """SELECT max(id) FROM data"""
    lastRow = mycursor.fetchone()  # the fetchone helps store the query in returnObject

    #next few lines are just for testing in later phases

    '''
    if lastRow:
        print(lastRow[0])
    else:
        print("Nothing found!")
    '''
    return lastRow


#ENTRY OF DATA
#note that the array contains the information input by the user
# here n is the sl no to be input at, where n-1 is the last filled up row.

def enterData(arr):

    slNo = checkLastRow()
    if slNo == None:
        slNo = 1

    dataEntry = """INSERT INTO data VALUES (%d, %s, %s, %s, %s, %s)"""%(slNo, arr[0], arr[1], arr[2], arr[3], arr[4])

    mycursor.execute(dataEntry)

    print("Data entry successful!!! We will remind you when to study this topic again")


#RETRIEVAL OF DATA


def retrieveData():

    dateToday = datetime.date.today()
    #print(dateToday)
    retrieval = '''SELECT topic FROM data WHERE date2 = %s OR date3 = %s OR date4 = %s ''' %(dateToday, dateToday, dateToday)
    mycursor.execute(retrieval)
    topicToStudy = mycursor.fetchone() #the fetchone helps store the query in returnObject

    notification.notify(
        title = "Spaced Repetition Reminder",
        message = topicToStudy + "\n You should take your time and revise this topic today.",
        # icon = "",
        timeout=10
        )

    '''
    if topicToStudy:
        return topicToStudy[0]
    else:
        return "Nothing found!"
    '''


#if __name__ == "__main__":

# define connection and cursor

connection = sqlite3.connect("data.db")  # connection is used to connect to the database // if db exists nothing new is created.
mycursor = connection.cursor()  # cursor is used to execute commands through the connection made

# mycursor.execute() command is used to execute mysql commands through the program

# TABLE CREATION IF IT DOESN'T ALREADY EXIST
createTable = """CREATE TABLE IF NOT EXISTS 
    data(id SMALLINT PRIMARYKEY, topic VARCHAR(30),date1 DATE,date2 DATE,date3 DATE,date4 DATE)"""

mycursor.execute(createTable)

while True:
    print("SELECT THE REQUIRED ACTION:")
    print("1. Add new data")
    print("2. Get reminded whatcha need to study today")
    userInput = int(input())
    #print(type(userInput))
    if userInput == 1:
        date = input("Enter date yyyy-mm-dd: ")
        topic = input("Enter the topic studied today: ")

        days_added = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        datee = datetime.datetime.strptime(date, "%Y-%m-%d")

        month = datee.month
        day = datee.day
        year = datee.year
        cultve_date = day

        cultve_date = day + days_added[month - 2]
        #print(cultve_date)
        x = str(day)
        y = str(month)  # These are just to store string value.Not important
        z = str(year)
        date1 = z + '-' + y + '-' + x

        # first notification
        first_notif = cultve_date + 1
        from datetime import datetime, date, timedelta

        # initializing day number
        day_num = first_notif

        converted_num = str(day_num)
        # adjusting day num
        converted_num.rjust(3 + len(converted_num), '0')

        # Initialize year
        yr = year

        # Initializing start date
        strt_date = date(yr, 1, 1)

        # converting to date
        res_date = strt_date + timedelta(days=int(converted_num) - 1)
        date2 = res_date.strftime("%Y-%m-%d")

        # second notification

        second_notif = cultve_date + 7

        conv_num = str(second_notif)

        conv_num.rjust(3 + len(conv_num), '0')
        rest_date = strt_date + timedelta(days=int(conv_num) - 1)
        date3 = rest_date.strftime("%Y-%m-%d")

        # third notification
        third_notif = cultve_date + 31
        con_num = str(third_notif)

        con_num.rjust(3 + len(con_num), '0')
        r_date = strt_date + timedelta(days=int(con_num) - 1)
        date4 = r_date.strftime("%Y-%m-%d")

        # aray
        # storing the data in the array
        data = [topic, date1, date2, date3, date4]
        # print(data)

        enterData(data) #FUNCTION CALL for entering data // NOT WORKING //

    elif userInput == 2:
        retrieveData()