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
    mycursor.execute(f"CALL opprettLån({elevID}, {bokID})")
    dbb.commit()

def updateEntry():
    elevID = entry_elev_ID.get()
    bokID = entry_bok_ID.get()
    mycursor.execute(f"CALL levertInn({elevID}, {bokID})")
    dbb.commit()

font = ("Comix Sans MS", 12)

root = tk.Tk()
entry_elev_ID = tk.Entry(root)
entry_elev_ID.grid(row = 1, column = 1)
entry_bok_ID = tk.Entry(root)
entry_bok_ID.grid(row = 2, column = 1)

tk.Label(root, text = "Legg inn elevens ID", font = font).grid(row = 1, column = 0)
tk.Label(root, text = "Legg inn bokens ID", font = font).grid(row = 2, column = 0)

add_btn = tk.Button(root, text = "Lån bok", font = font, command = addEntry)
add_btn.grid(row = 3, column = 1)

update_btn = tk.Button(root, text = "Lever inn bok", font = font, command = updateEntry)
update_btn.grid(row = 4, column = 1)

root.mainloop()