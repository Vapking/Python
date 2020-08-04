import mysql.connector

try:

	conn = mysql.connector.connect(host = "localhost",user = "vivek",passwd = "1234",database = "MyDB")
	cur = conn.cursor()  
	cur.execute("alter table student add mobile_no varchar(10)")

except Exception as e:
	print("Error : ",e)

finally:
	conn.close()	
