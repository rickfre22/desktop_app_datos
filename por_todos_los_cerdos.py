from tkinter import *
ventana = Tk()
ventana.title("id")
ventana.geometry("400x345")
ventana.config(bg="white")
ventana.resizable(False,False)

titulo = Label(ventana,text="Miguel Angel Galvis Quiñonez")
titulo.config(bg="white",fg="black",font=("script",15))
titulo.place(x=0,y=0)
foto =PhotoImage(file="img/foto.png")
lb_foto=Label(ventana,image=foto,bg="white")
lb_foto.place(x=20,y=20)
ventana.mainloop()