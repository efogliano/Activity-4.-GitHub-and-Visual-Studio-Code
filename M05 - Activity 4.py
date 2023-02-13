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


    #Linies
    canvas.create_line(amplada*0.1,altura*0.9,amplada*0.5,altura*0.1)
    canvas.create_line(amplada*0.5,altura*0.1,amplada*0.9,altura*0.9)
    canvas.create_line(amplada*0.1,altura*0.9,amplada*0.9,altura*0.9)



    canvas.pack()
    mainloop()
    print("oi")
#Jaume

#Main
print("prova")
triangle()