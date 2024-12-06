from tkinter import *
raam = Tk()
raam.title("lipp")
tahvel = Canvas(raam, width=1000, height=500)

tahvel.create_rectangle(0, 225, 1000, 0, outline="#301BA6", fill="#301BA6")
tahvel.create_rectangle(0, 275, 1000, 500, outline="#AC5D06", fill="#AC5D06")
tahvel.create_rectangle(0, 200, 1000, 300, outline="white", fill="white")

tahvel.pack()
raam.mainloop()
