import mysql.connector

try :
	conn = mysql.connector.connect(host ="localhost",user = "vivek",passwd = "1234",database = "MyDB")
	cur = conn.cursor()
	print(cur)
except Exception as e :
		print("Error : ",e)

finally :
		conn.close()