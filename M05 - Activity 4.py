#Eloy

#Arnau
def triangle():
    from tkinter import Tk, Canvas, Button, mainloop
    #parametres d'alçada i amplada per fer finestra variable
    altura=600
    amplada=500
    # mesCares = percentatgeCares*altura/100 → Calcula amb percentatge la coordenada, útil per responsive



    finestra = Tk() #Finestra Tk Inter per dibuixar a dintre
    canvas = Canvas(finestra, width=amplada, height=altura, background="grey")

    #Text
    canvas.create_text(amplada*0.3,altura-mesCreus-altura*0.01, text="Creus")


    #Linies
    canvas.create_line(amplada*0.2,altura*0.2,amplada*0.4,altura*0.4)



    canvas.pack()
#Jaume