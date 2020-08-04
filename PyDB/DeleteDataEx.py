import mysql.connector 

try : 
	conn = mysql.connector.connect(host = "localhost",user = "vivek",passwd = "1234",database = "MyDB")
	cur = conn.cursor()

	cur.execute("delete from student where rollno = 5")
	conn.commit()
	
	print(cur.rowcount," Record Deleted!")

except Exception as e :
	print("Error : ",e)

finally:
	conn.close()