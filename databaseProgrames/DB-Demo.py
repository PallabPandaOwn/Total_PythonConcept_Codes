

import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', passwd="1234",database='teluskoTest')
mycursor= mydb.cursor()
# mycursor.execute("show databases")

# mycursor.execute("use teluskoTest")
mycursor.execute("select Name from student")

for i in mycursor:
    print(i)