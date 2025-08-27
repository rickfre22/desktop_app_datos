from tkinter import *

ventana =Tk()
ventana.title("datos")
ventana.geometry("400x400")
ventana.config(bg="white")
# funciones
def ventana_1():
    global ventana_1
    ventana_1 =Toplevel()
    ventana_1.title("Fecha")
    ventana_1.geometry("200x100")
    ventana_1.config(bg="white")
    Label(ventana_1,text="altura:1,68m\n " \
    "peso:49kg\n" \
    "TS:A+\n" \
    "seguro:Nueva eps",bg="white").pack(pady=0)

bt_fecha = Button(ventana, text="datos medicos",command=ventana_1)
bt_fecha.place(x=10, y=140, width=100, height=30)


def ventana_2():
    global ventana_2
    ventana_2 =Toplevel()
    ventana_2.title("Fecha")
    ventana_2.geometry("200x100")
    ventana_2.config(bg="white")
    Label(ventana_2,text="22/03/2010\n " \
    "hospital regional de sangil",bg="white").pack(pady=0)

bt_datosme = Button(ventana, text="nacimiento",command=ventana_2)
bt_datosme.place(x=120, y=140, width=100, height=30)

def ventana_3():
    global ventana_3
    ventana_3 =Toplevel()
    ventana_3.title("Fecha")
    ventana_3.geometry("280x200")
    ventana_3.config(bg="white")
    Label(ventana_3,text="mis padres:\n " \
    "Oscar ivan galvis rincon(edad:33)\n" \
    "Liliana quiñonez quiñonez(edad:36)\n" \
    "mis hermanos\n" \
    "kevin alejandro quiñonez quiñonez(edad:17)\n" \
    "juan jose diaz quiñonez(edad:18)\n" \
    "y yo\n" \
    "miguel angel galvis quiñonez(edad:15)",bg="white").pack(pady=0)

bt_familia = Button(ventana, text="familia",command=ventana_3)
bt_familia.place(x=230, y=140, width=100, height=30)

def ventana_4():
    global ventana_4
    ventana_4 =Toplevel()
    ventana_4.title("Fecha")
    ventana_4.geometry("280x80")
    ventana_4.config(bg="white")
    Label(ventana_4,text="todo mi proceso es en el colegiio guanenta \ndesde 1° hasta 10°(actual)",bg="white").pack(pady=0)

bt_procesoedu = Button(ventana, text="proceso educativo",command=ventana_4)
bt_procesoedu.place(x=10, y=180, width=130, height=30)

def ventana_5():
    global ventana_5
    ventana_5 =Toplevel()
    ventana_5.title("amigos")
    ventana_5.geometry("250x150")
    ventana_5.config(bg="white")
    Label(ventana_5,text="soreth(15 años)\n" \
    "juan pablo(15 años)\n" \
    "juan fernando(15 años)\n" \
    "jorge silva(15 años)\n" \
    "samir archila(16 años)\n" \
    "harold martinez(15)\n" \
    "oscar sanches(16)",bg="white").pack(pady=0)

bt_amigos = Button(ventana, text="amigos",command=ventana_5)
bt_amigos.place(x=150, y=180, width=100, height=30)
def ventana_6():
    global ventana_6
    ventana_6 =Toplevel()
    ventana_6.title("Fecha")
    ventana_6.geometry("200x100")
    ventana_6.config(bg="white")
    Label(ventana_6,text="hobbies:\njugar videojuegos",bg="white").pack(pady=0)

bt_hobbies = Button(ventana, text="hobbies",command=ventana_6)
bt_hobbies.place(x=260, y=180, width=100, height=30)
 
def ventana_7():
    global ventana_7
    ventana_7 =Toplevel()
    ventana_7.title("Fecha")
    ventana_7.geometry("350x100")
    ventana_7.config(bg="white")
    Label(ventana_7,text="lunes martes miercoles jueves viernes sabado domingo\ncolegio----- especiaidad y colegio ------------ banda---descanso",bg="white").pack(pady=0)
bt_horario = Button(ventana, text="horario",command=ventana_7)
bt_horario.place(x=10, y=220, width=100, height=30)
def ventana_8():
    global ventana_8
    ventana_8 =Toplevel()
    ventana_8.title("Fecha")
    ventana_8.geometry("200x100")
    ventana_8.config(bg="white")
    Label(ventana_8,text="con base a lo aprendidon el colegio\n esa sera mi preracion",bg="white").pack(pady=0)
bt_datosme = Button(ventana, text="preracion icfes",command=ventana_8)
bt_datosme.place(x=120, y=220, width=100, height=30)

def ventana_9():
    global ventana_9
    ventana_9 =Toplevel()
    ventana_9.title("Fecha")
    ventana_9.geometry("200x100")
    ventana_9.config(bg="white")
    Label(ventana_9,text="ya haberme graduado de\n licenciatura en musica\ny empezar el doctorado\n obviamente en musica",bg="white").pack(pady=0)
bt_datosme = Button(ventana, text="proyecto de vida 2031",command=ventana_9)
bt_datosme.place(x=230, y=220, width=150, height=30)

def ventana_10():
    global ventana_10
    ventana_10 =Toplevel()
    ventana_10.title("Fecha")
    ventana_10.geometry("200x100")
    ventana_10.config(bg="white")
    Label(ventana_10,text="a mi me gusta la musica,\n la trompeta, y \nlos demas vientos metal, ",bg="white").pack(pady=0)
bt_datosme = Button(ventana, text="mis gustos",command=ventana_10)
bt_datosme.place(x=20, y=260, width=100, height=30)
# frame perfil
frame_1 =(Frame(ventana))
frame_1.config(bg="red",width=100,height=133)
frame_1.place(x=-1,y=-1)
titulo = Label(ventana, text="Miguel Angel Galvis Quiñonez")
titulo.config(bg = "white",fg="black", font=("arial", 16))
titulo.place(x=100,y=25)

titulo_2 = Label(ventana,text="Nombre:")
titulo_2.config(bg = "white",fg="black", font=("arial", 16))
titulo_2.place(x=100,y=0)

titulo3 = Label(ventana, text="15\nID:1100 960 949")
titulo3.config(bg = "white",fg="black", font=("arial", 16))
titulo3.place(x=100,y=55)

titulo_4 = Label(ventana,text="Edad:")
titulo_4.config(bg = "white",fg="black", font=("arial", 16))
titulo_4.place(x=100,y=55)



perfil = PhotoImage(file="img/perfil.png")
lb_perfil=Label(frame_1,image=perfil,bg="pink")
lb_perfil.place(x=0,y=0)

ventana.mainloop()