import mysql.connector 

dbb = mysql.connector.connect(
    host= "localhost",
    user= "root",
    password = "mysql",
    database = "mydeebee")
mycursor = dbb.cursor()
