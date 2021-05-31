import sqlite3
import datetime

#define connection and cursor

connection = sqlite3.connect("data.db") #connection is used to connect to the database
mycursor = connection.cursor() #cursor is used to execute commands through the connection made

# mycursor.execute() command is used to execute mysql commands in the program


#TABLE CREATION IF IT DOESN'T ALREADY EXIST
createTable = """CREATE TABLE IF NOT EXISTS 
    data(id SMALLINT PRIMARYKEY, topic VARCHAR(30),date1 DATE,date2 DATE,date3 DATE,date4 DATE)"""

#mycursor.execute(createTable)



#ENTRY OF DATA
#note that the array contains the information input by the user
# here n is the sl no to be input at, where n-1 is the last filled up row.
dataEntry = """INSERT INTO data VALUES (n, %s, %s, %s, %s, %s)"""

#mycursor.execute(dataEntry)



#RETRIEVAL OF DATA
dateToday = datetime.date.today()
#print(dateToday)
'''
now use this to compare with the dates existing in the database
next use the corresponding topic to the date to find which subject to study
'''




#UPDATING INFROMATION



