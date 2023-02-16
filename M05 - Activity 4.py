#Eloy
print("M05 - ACTIVITY 4")

#This function will display a figure when the answer is correct.
def Congrats():
    from tkinter import Tk, Canvas, Button, mainloop
    w = 500
    h = 500
    finestra = Tk()
    canvas = Canvas(finestra, width=w, height=h, \
    background="white")
    canvas.create_oval(10,10,490,490, fill="green")
    canvas.pack()
    mainloop()

#This function will display a figure when the answer is incorrect.
def Incorrect():
    from tkinter import Tk, Canvas, Button, mainloop
    w = 500
    h = 500
    finestra = Tk()
    canvas = Canvas(finestra, width=w, height=h, \
        background="white")
    canvas.create_line(10,10,500,500,fill="red", width=50)
    canvas.create_line(500,10,10,500,fill="red", width=50)
    canvas.pack()
    mainloop()

#Arnau

#Jaume

#MAIN

#Show Figure1
try:
    answer = int (input("How many triangles are there in the following figure?"))
    if answer == 24: 
        valid=True
    else: 
        valid=False
except:
    print("Incorrect format, a number must be entered.")

if valid:
    print("Congratulations!")
    Congrats()
else:
    print("Is wrong...")
    Incorrect()

#Show Figure2
try:
    answer = int (input("How many squares are there in the following figure?"))
    if answer == 20: 
        valid=True
    else: 
        valid=False
except:
    print("Incorrect format, a number must be entered.")

if valid:
    print("Congratulations!")
    Congrats()
else:
    print("Is wrong...")
    Incorrect()