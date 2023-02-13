#Eloy

#Arnau
def triangle():
    from tkinter import Tk, Canvas, Button, mainloop
    #parametres d'altura i amplada per fer finestra variable
    print("How big do you want the windows?")
    altura=500
    amplada=500
    # mesCares = percentatgeCares*altura/100 -> Calcula amb percentatge la coordenada, util per responsive



    finestra = Tk() #Finestra Tk Inter per dibuixar a dintre
    canvas = Canvas(finestra, width=amplada, height=altura, background="grey")

    #Text
    canvas.create_text(amplada*0.5,altura*0.05, text="How many Triangles")


    #Basic Linies
    canvas.create_line(amplada*0.1,altura*0.9,amplada*0.5,altura*0.1)
    canvas.create_line(amplada*0.5,altura*0.1,amplada*0.9,altura*0.9)
    canvas.create_line(amplada*0.1,altura*0.9,amplada*0.9,altura*0.9)

    #Interior Horizontal
    canvas.create_line(amplada*0.4,altura*0.3,amplada*0.6,altura*0.3)
    canvas.create_line(amplada*0.3,altura*0.5,amplada*0.7,altura*0.5)
    canvas.create_line(amplada*0.2,altura*0.7,amplada*0.8,altura*0.7)

    #Interior Vertical
    canvas.create_line(amplada*0.35,altura*0.9,amplada*0.5,altura*0.1)
    canvas.create_line(amplada*0.5,altura*0.1,amplada*0.65,altura*0.9)

    canvas.pack()
    mainloop()
#Jaume

#Main
print("prova")
triangle()