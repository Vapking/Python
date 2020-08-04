import mysql.connector

try:

	conn = mysql.connector.connect(host = "localhost",user = "vivek",passwd = "1234")
	cur = conn.cursor()  
	cur.execute("show databases")
	
	result = cur.fetchall()

	print("**** DataBase Names ****")
	
	for i in result :
		print(i)
	
except Exception as e:
	print("Error : ",e)

finally:
	conn.close()	
