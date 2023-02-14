#Eloy

#Arnau
#Function to get a positive value
def GetPositiveValue():
    pixels=0
    correct=False
    while not correct:
        try:
            pixels=int(input())
            if pixels>0:
                correct=True
            else: print("Enter a valid number bigger than 0")
        except:
            print("Enter a valid number bigger than 0")
    return pixels

#Function of the Triangle Problem
def Triangle():
    from tkinter import Tk, Canvas, Button, mainloop
    #parametres of width and height for the drawing window
    print("How big do you want the emerging window?")
    print("The width in pixels")
    altura=GetPositiveValue()
    print("The height in pixels")
    amplada=GetPositiveValue()
    # mesCares = percentatgeCares*altura/100 -> Calcula amb percentatge la coordenada, util per responsive

    window = Tk() #Drawing window of Tk Inter
    canvas = Canvas(window, width=amplada, height=altura, background="grey")

    #Text
    canvas.create_text(amplada*0.5,altura*0.05, text="How many Triangles in total?")

    #Main Triangle Lines
    canvas.create_line(amplada*0.1,altura*0.9,amplada*0.5,altura*0.1)
    canvas.create_line(amplada*0.5,altura*0.1,amplada*0.9,altura*0.9)
    canvas.create_line(amplada*0.1,altura*0.9,amplada*0.9,altura*0.9)

    #Interior Horizontal Lines
    canvas.create_line(amplada*0.4,altura*0.3,amplada*0.6,altura*0.3)
    canvas.create_line(amplada*0.3,altura*0.5,amplada*0.7,altura*0.5)
    canvas.create_line(amplada*0.2,altura*0.7,amplada*0.8,altura*0.7)

    #Interior Vertical Lines
    canvas.create_line(amplada*0.35,altura*0.9,amplada*0.5,altura*0.1)
    canvas.create_line(amplada*0.5,altura*0.1,amplada*0.65,altura*0.9)

    canvas.pack()
    mainloop()
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

#Main
Triangle()