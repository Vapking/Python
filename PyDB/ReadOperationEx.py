import mysql.connector

try :
	conn = mysql.connector.connect(host = "localhost",user = "vivek" ,passwd = "1234" ,database = "MyDB")
	cur = conn.cursor() 

	cur.execute("select rollno,name,dept_name,mobile_no from student")
	result = cur.fetchall()

	print("Roll No.\tName\tDepartment Name\tMobile No.")
	for col in result:
		print("|%s\t\t|%s\t|%s\t\t|%s|"%(col[0],col[1],col[2],col[3]))
	
except Exception as e :
	print("Error : ",e)

finally:
	conn.close()