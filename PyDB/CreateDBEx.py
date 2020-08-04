import mysql.connector

try:

	conn = mysql.connector.connect(host = "localhost",user = "vivek",passwd = "1234")
	cur = conn.cursor()  
	cur.execute("CREATE DATABASE MyDB")

	cur.execute("show databases")
	
	print("**** Database Names ****")
	for i in cur:
		print(i)

except Exception as e:
	print("Error : ",e)

finally:
	conn.close()	
