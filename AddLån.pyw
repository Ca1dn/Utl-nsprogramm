import mysql.connector 

dbb = mysql.connector.connect(
    host= "localhost",
    user= "root",
    password = "mysql",
    database = "mydeebee"
)

mycursor = dbb.cursor()

def addEntry():
    elevID = entry_elev_ID.get()
    bokID = entry_bok_ID.get()
    mycursor.execute("CALL opprettLån(elevID, bokID)")
    mydeebee.commit()

def updateEntry():
    elevID = entry_elev_ID.get()
    bokID = entry_bok_ID.get()
    mycursor.execute("CALL levertInn(elevID, bokID)")
    mydeebee.commit()