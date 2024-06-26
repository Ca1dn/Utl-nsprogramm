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
    lånt_tilbakemelding()
    elevID = entry_elev_ID.get()
    bokID = entry_bok_ID.get()
    mycursor.execute(f"CALL opprettLån({elevID}, {bokID})")
    dbb.commit()

def updateEntry():
    elevID = entry_elev_ID.get()
    bokID = entry_bok_ID.get()
    mycursor.execute(f"CALL levertInn({elevID}, {bokID})")
    dbb.commit()

font = ("Helvetica", 14)

def lånt_tilbakemelding():
    if not har_gitt_tilbakemelding.get():
        har_gitt_tilbakemelding.set(True)
        tilbakemelding.config(text = "Du har lånt en bok⁉", font = font, bg='lightGreen')
        root.after(3000, lånt_tilbakemelding)
    else:
        har_gitt_tilbakemelding.set(False)
        tilbakemelding.config(text = "", bg='lightgrey')

root = tk.Tk()
root.geometry("400x150")  
root.title("Lån bok")
root.configure(bg='lightgrey')

entry_elev_ID = tk.Entry(root, font=font, bg='grey')
entry_elev_ID.grid(row=1, column=1)
entry_bok_ID = tk.Entry(root, font=font, bg='grey')
entry_bok_ID.grid(row=2, column=1)

tk.Label(root, text="Legg inn elevens ID", font=font, bg='lightgrey').grid(row=1, column=0)
tk.Label(root, text="Legg inn bokens ID", font=font, bg='lightgrey').grid(row=2, column=0)

add_btn = tk.Button(root, text="Lån bok", font=font, command=addEntry, padx=2, pady=2, bg='LightGreen')
add_btn.grid(row=3, column=1, pady=4)

update_btn = tk.Button(root, text="Lever inn bok", font=font, command=updateEntry, padx=2, pady=2, bg='LightCoral')
update_btn.grid(row=4, column=1)

har_gitt_tilbakemelding = tk.BooleanVar()
har_gitt_tilbakemelding.set(False)
tilbakemelding = tk.Label(root)
tilbakemelding.grid(row=3, column=-0, columnspan=1)
tilbakemelding.config(bg='lightgrey')

root.mainloop()
