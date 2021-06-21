from tkinter import *
from datetime import datetime

raiz= Tk()
raiz.geometry("400x450+100+300")
raiz.title("Cronometro")
raiz.config(bg='#FF0000')
raiz.resizable(False, False)

boton_inicio= Button(raiz, text="Iniciar",
width=12, command=lambda:comienza_cuenta(etiq))
boton_inicio.place(x=30, y=390)

contador = 0
transcurso=False

def etiq_contador(label):
    def contar():
        if transcurso:
            global contador
            if contador == 0:
                display='00'
            else:
                display=str(contador)

            label["text"]=display

            label.after(1000, contar)
            contador += 1
    
    contar()

def comienza_cuenta(label_1):
    global transcurso
    transcurso = True
    etiq_contador(label_1)
    boton_inicio["state"]="disabled"
    boton_detener['state']='normal'
    boton_resetear['state']='normal'

def detiene_cuenta():
    global transcurso
    boton_inicio["state"]="normal"
    boton_detener['state']='disabled'
    boton_resetear['state']='normal'
    transcurso=False

def reinicio(label_2):
    global contador
    contador = 0
    if transcurso==False:
        boton_resetear["state"]="disabled"
        label_2["text"]='00'
    else:
        label_2["text"]=''

etiq = Label(raiz, text='00', fg='black', bg='#FF0000',
font="Verdana 40 bold")

etiq_mnts= Label(raiz, text='Tiempo', fg='black',
bg='#FF0000', font="Verdana 10 bold")

etiq.place(x=160, y=170)
etiq_mnts.place(x=170, y=250)

boton_detener=Button(raiz, text='Detener', width=12, state='disabled',
command=detiene_cuenta)

boton_resetear=Button(raiz, text='Reiniciar', width=12, state='disabled',
command=lambda:reinicio(etiq))

boton_detener.place(x=150, y=390)
boton_resetear.place(x=270, y=390)

raiz.mainloop()