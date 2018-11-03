import math
import psycopg2
import csv
import secret
import os
#Menu program.
print("Geting timg###.png Data.")
print("For testdata.csv")
#email = input("Enter the email for the user\n")
query = """
    select *
    FROM picpoints
    WHERE imgname LIKE 'timg%'
    """



#print(query)   #Debug purposes.

#print(myMail)  #Debug purposes.
connection = "host = 'localhost' dbname = 'learningflask' user='"+secret.theUser + "'  password='" + secret.theSecret + "'"
print("Connecting to database...")
conn = psycopg2.connect(connection)
cursor = conn.cursor()
#cursorX = conn.cursor()
flag = False
try:
    cursor.execute(query)
    print("\nAttempt Successful\n")
    flag = True
except:
    print("\nNo Query available\n")
    flag = False
rows = cursor.fetchall()
print("Number of rows\n")
print(len(rows))
numberOfRows = len(rows)
if(numberOfRows):
    output = "COPY ({0}) TO STDOUT WITH CSV HEADER".format(query)

    saveFileName = 'testData.csv'

    with open(saveFileName,'w') as f:
        cursor.copy_expert(output,f)
else:
    print("No Data to report.")

conn.close()
