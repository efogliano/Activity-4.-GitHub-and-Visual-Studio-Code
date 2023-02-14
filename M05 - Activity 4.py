#Eloy

#Arnau

#Jaume
def HowManySquares():
    from tkinter import Tk, Canvas, Button, mainloop

    WIDTH=600
    HEIGHT=700

    finestra = Tk()
    canvas = Canvas(finestra, width=WIDTH, height=HEIGHT, background="white")
    canvas.pack()

    canvas.create_text(300, 50, text="HOW MANY SQUARES CAN YOU FIND?", font=('Arial',20), fill="black")
    #Quadrats superior esquerra 
    canvas.create_rectangle(0,100,150,250, width=2, fill="grey")
    canvas.create_rectangle(150,100,300,250, width=2, fill="grey")
    canvas.create_rectangle(0,250,150,400, width=2, fill="grey")
    canvas.create_rectangle(150,250,300,400, width=2, fill="grey")
    #Quadrats superior dreta
    canvas.create_rectangle(300,100,450,250, width=2, fill="grey")
    canvas.create_rectangle(450,100,600,250, width=2, fill="grey")
    canvas.create_rectangle(300,250,450,400, width=2, fill="grey")
    canvas.create_rectangle(450,250,600,400, width=2, fill="grey")
    #Quadrats inferior esquerra
    canvas.create_rectangle(0,400,150,550, width=2, fill="grey")
    canvas.create_rectangle(150,400,300,550, width=2, fill="grey")
    canvas.create_rectangle(0,550,150,700, width=2, fill="grey")
    canvas.create_rectangle(150,550,300,700, width=2, fill="grey")
    #Quadrats inferior dreta
    canvas.create_rectangle(300,400,450,550, width=2, fill="grey")
    canvas.create_rectangle(450,400,600,550, width=2, fill="grey")
    canvas.create_rectangle(300,550,450,700, width=2, fill="grey")
    canvas.create_rectangle(450,550,600,700, width=2, fill="grey")
    #Quadrats en diagonal
    canvas.create_rectangle(75,175,225,325, width=2, fill="grey")
    canvas.create_rectangle(225,325,375,475, width=2, fill="grey")
    canvas.create_rectangle(375,475,525,625, width=2, fill="grey")
    #Línies quadrats en diagonal
    canvas.create_line(375,550,525,550, width=2, fill="black")
    canvas.create_line(450,475,450,625, width=2, fill="black")
    #Línies quadrats en diagonal
    canvas.create_line(225,400,375,400, width=2, fill="black")
    canvas.create_line(300,325,300,475, width=2, fill="black")
    #Línies quadrats en diagonal
    canvas.create_line(75,250,225,250, width=2, fill="black")
    canvas.create_line(150,175,150,325, width=2, fill="black")

    mainloop()