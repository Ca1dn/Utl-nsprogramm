import mysql.connector 
import tkinter as tk

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
    dbb.commit()

def updateEntry():
    elevID = entry_elev_ID.get()
    bokID = entry_bok_ID.get()
    mycursor.execute("CALL levertInn(elevID, bokID)")
    dbb.commit()

root = tk.Tk()
entry_elev_ID = tk.Entry(root)
entry_elev_ID.grid(row = 1, column = 1)
entry_bok_ID = tk.Entry(root)
entry_bok_ID.grid(row = 2, column = 1)

tk.Label(root, text = "Legg inn elevens ID").grid(row = 1, column = 0)
tk.Label(root, text = "Legg inn bokens ID").grid(row = 2, column = 0)
