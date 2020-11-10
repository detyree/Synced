from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title('Picture Viewer v. 1.0')
root.geometry("400x400")

my_img = ImageTk.PhotoImage(Image.open("name of picture"))
my_label = Label(image=my_img)
my_label.pack()






root.mainloop()

'''# Database pieces

# Create User Pictures DB
conn = sqlite3.connect('User_Info.db')

# Create a cursor

c = conn.cursor()

#Create Table
c.execute("""CREATE TABLE UserInfo (
    first_name text,
    last_name text,
    phone_number text,
    age int,
    email text
    )""")



#Commit Changes
conn.commit()
#Close Connection
conn.close()
'''
