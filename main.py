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
janela.geometry("235x305")
janela.config(bg=cor1)

#Frames
frame_tela = Frame(janela, width=300, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=300, height=268)
frame_corpo.grid(row=1, column=0)

#Variável para todos os valores recebido

valores_recebidos = ''

#criando função 

def entrada_valores(event):

    global valores_recebidos
    valores_recebidos = valores_recebidos + str(event)

    #passando valor para a tela
    valor_texto.set(valores_recebidos)

#Criando label
valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)

#Botões

b_clear = Button(frame_corpo, text="C", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_clear.place(x=0, y=0)

b_modulo = Button(frame_corpo, command = lambda: entrada_valores('%'), text="%", width=5, height=2, bg=cor4,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_modulo.place(x=118, y=0)

b_divisao = Button(frame_corpo, command = lambda: entrada_valores('/'), text="/", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_divisao.place(x=177, y=0)


b_7 = Button(frame_corpo, command = lambda: entrada_valores('7'),text="7", width=5, height=2, bg=cor4,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=0, y=51)

b_8 = Button(frame_corpo, command = lambda: entrada_valores('8'),text="8", width=5, height=2, bg=cor4,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=59, y=51)

b_9 = Button(frame_corpo, command = lambda: entrada_valores('9'),text="9", width=5, height=2, bg=cor4,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=118, y=51)

b_divisao = Button(frame_corpo, command = lambda: entrada_valores('*'),text="*", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_divisao.place(x=177, y=51)


b_4 = Button(frame_corpo, command = lambda: entrada_valores('4'),text="4", width=5, height=2, bg=cor4,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=102)

b_5 = Button(frame_corpo, command = lambda: entrada_valores('5'),text="5", width=5, height=2, bg=cor4,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=102)

b_6 = Button(frame_corpo, command = lambda: entrada_valores('6'),text="6", width=5, height=2, bg=cor4,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=102)

b_divisao = Button(frame_corpo, command = lambda: entrada_valores('/'),text="-", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_divisao.place(x=177, y=102)


b_1 = Button(frame_corpo, command = lambda: entrada_valores('1'),text="1", width=5, height=2, bg=cor4,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=153)

b_2 = Button(frame_corpo, command = lambda: entrada_valores('2'),text="2", width=5, height=2, bg=cor4,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=59, y=153)

b_3 = Button(frame_corpo, command = lambda: entrada_valores('3'),text="3", width=5, height=2, bg=cor4,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=118, y=153)

b_adicao = Button(frame_corpo, command = lambda: entrada_valores('+'),text="+", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_adicao.place(x=177, y=153)


b_0 = Button(frame_corpo, command = lambda: entrada_valores('0'),text="0", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_0.place(x=0, y=204)

b_ponto = Button(frame_corpo, command = lambda: entrada_valores('.'),text=".", width=5, height=2, bg=cor4,  font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_ponto.place(x=118, y=204)

b_igual = Button(frame_corpo, command = lambda: entrada_valores('='),text="=", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_igual.place(x=177, y=204)


janela.mainloop()



