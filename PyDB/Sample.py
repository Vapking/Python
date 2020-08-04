import mysql.connector

mydb = mysql.connector.connect(host = "localhost",user = "vivek",passwd = "1234",database = "mydb")

mycursor = mydb.cursor()