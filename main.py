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

frame_tela = Frame(janela, width=235, height=50)
frame_tela.grid(row=0, column=0)

janela.mainloop()



