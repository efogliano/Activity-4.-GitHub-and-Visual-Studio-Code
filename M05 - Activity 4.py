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

#Main
Triangle()