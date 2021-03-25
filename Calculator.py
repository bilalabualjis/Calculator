# from Calculator.py import *
from tkinter import *

wind = Tk()
wind.title("calculator")
wind.geometry("300x400")

text = Entry(wind,font=("calibri", 16))
text.pack(fill=X,padx=5,ipadx=5,ipady=5)


frame = Frame(wind)
frame.pack(side=TOP,anchor=NW)

rightFrame = Frame(frame)
rightFrame.pack(side=RIGHT)

frame1 = Frame(frame)
frame1.pack()

#btn 1 to 3
btn1 = Button(frame1,text="1",width=9,height=3)
btn1.pack(side=LEFT)


wind.mainloop()