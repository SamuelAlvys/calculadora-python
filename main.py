#Importando o Tkinter
from tkinter import *
from tkinter import ttk

#Cores
cor1 = "#3B3B3B" # preto
cor2 = "#FEFFFF" # branco
cor3 = "#38576B" # azul
cor4 = "#ECEFF1" # cinza
cor5 = "#FFAB40" # laranja

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(bg=cor1)

#Frames
frame_tela = Frame(janela, width=300, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=300, height=268)
frame_corpo.grid(row=1, column=0)

#Botões

b_clear = Button(frame_corpo, text="C", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_clear.place(x=0, y=0)

b_modulo = Button(frame_corpo, text="%", width=5, height=2, bg=cor4,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_modulo.place(x=118, y=0)

b_divisao = Button(frame_corpo, text="/", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_divisao.place(x=177, y=0)

janela.mainloop()



