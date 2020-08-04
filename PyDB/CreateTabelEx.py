import mysql.connector

try:

	conn = mysql.connector.connect(host = "localhost",user = "vivek",passwd = "1234",database = "MyDB")
	cur = conn.cursor()  
	cur.execute("create table student(id int(11) primary key auto_increment,name varchar(1000) not null,rollno int not null,dept_name varchar(100) not null)")

except Exception as e:
	print("Error : ",e)

finally:
	conn.close()	
