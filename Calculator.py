# from Calculator.py import *
from tkinter import *

wind = Tk()
wind.title("calculator")
wind.geometry("300x400")

text = Entry(wind,font=("calibri", 16))
text.pack(fill=X,padx=5,ipadx=5,ipady=5)

def addToText(n):
    text.insert(END,n)

frame = Frame(wind)
frame.pack(side=TOP,anchor=NW)

rightFrame = Frame(frame)
rightFrame.pack(side=RIGHT)

frame1 = Frame(frame)
frame1.pack()

#btn 1 to 3
btn1 = Button(frame1,text="1",width=9,height=3, command=lambda:addToText("1"))
btn1.pack(side=LEFT)
btn2 = Button(frame1,text="2",width=9,height=3, command=lambda:addToText("2"))
btn2.pack(side=LEFT)
btn3 = Button(frame1,text="3",width=9,height=3, command=lambda:addToText("3"))
btn3.pack(side=LEFT)


frame2 = Frame(frame)
frame2.pack()

#btn 4 to 6
btn4 = Button(frame2,text="4",width=9,height=3, command=lambda:addToText("4"))
btn4.pack(side=LEFT)
btn5 = Button(frame2,text="5",width=9,height=3, command=lambda:addToText("5"))
btn5.pack(side=LEFT)
btn6 = Button(frame2,text="6",width=9,height=3, command=lambda:addToText("6"))
btn6.pack(side=LEFT)

wind.mainloop()