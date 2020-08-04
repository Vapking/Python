import mysql.connector

try:

	conn = mysql.connector.connect(host = "localhost",user = "vivek",passwd = "1234",database = "MyDB")
	cur = conn.cursor() 

	sql = "insert into student(rollno,name,dept_name,mobile_no)values(%s,%s,%s,%s)"
	val = [(2,"Raju","E&TC","9876543210"),(3,"Nitin","CSE","9786453120"),(4,"Asazad","CSE","7984651302")]

	cur.executemany(sql,val)
	conn.commit()
	
	print(cur.rowcount," Record Inserted !")

except Exception as e:
	print("Error : ",e)

finally:
	conn.close()	
