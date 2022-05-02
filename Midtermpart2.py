from tkinter import *
from openpyxl import workbook, load_workbook
import pandas as pd
from PIL import Image, ImageTk
import random
import converter


root = Tk()
root.title('Convert your weight from LBS to KG')
root.geometry("500x300")
root.config(bg="#008B8B")
root.resizable(0, 0)




label1 = Label(text="Enter LBS:", bg="#76EE00")
label1.place(x=50, y=30)


textbox1 = Entry(width=12, bg="#76EE00")
textbox1.place(x=200, y=35)

label2 = Label( text="KG:", bg="#76EE00")
label2.place(x=50, y=100)

label3 = Label( text=" ", bg="#008B8B")
label3.place(x=180, y=100)




def lbstokg():
    pounds = round(float(textbox1.get()) *0.453592, 5)
    label3.configure(text=str(pounds) + '  Kilograms')



button1 = Button( text="Click Me To Convert", bg="#76EE00", command=lbstokg)
button1.place(x=90, y=150)


root.mainloop()
