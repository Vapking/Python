import mysql.connector

try :
	conn = mysql.connector.connect(host = "localhost",user = "vivek",passwd = "1234",database = "MyDB")
	cur = conn.cursor()
	
	MB_No = input("Enter Mobile No. : ")
	Rno = int(input("Enter Roll No of Which edit Mobile Number : "))
	
	cur.execute("update student set mobile_no = %s where rollno = %s"%(MB_No,Rno))
	conn.commit()
	
	print(cur.rowcount," Row Updated!")

except Exception as e :
	print("Error : ",e)

finally:
	conn.close()	