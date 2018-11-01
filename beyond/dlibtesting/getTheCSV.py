import math
import psycopg2
import csv
import secret
import os
#Menu program.
print("Welcome to the data delivery script, type in the user email, for the data you want.")
print("For what user?")
email = input("Enter the email for the user\n")
query = """
    select picpoints.*, scores.score, scores.email
    FROM picpoints
    INNER JOIN scores ON (picpoints.imgName = scores.imagename and scores.email =
    """

numOfRowsRequested = input("\nHow many rows do you need?\n")

#Deals with if their is a number of rows requested.
if(int(numOfRowsRequested) < 30):
    print("Getting at least 30, your number is too small.\n")
    numOfRowsRequested = 30
else:
    print("Modifying Query...")

query += " '" + email + "') "
query += " ORDER BY scores.id desc "
query += " LIMIT "
query += str(numOfRowsRequested)
#print(query)   #Debug purposes.
myMail = " '" + email + "') "
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
    email = email.replace("@","_")
    saveFileName = email + '-' + 'resultsfile.csv'
    direct = os.getcwd()
    path = os.path.join(direct+"/fileRecords/", saveFileName)

    with open(path,'w') as f:
        cursor.copy_expert(output,f)
else:
    print("No Data to report.")

conn.close()
