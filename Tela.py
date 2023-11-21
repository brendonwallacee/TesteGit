from tkinter import *
from Medicamento import Medicamento

janela = Tk()
janela.title("Testando entrada no Python")
janela.geometry('550x250')


lnome = Label(janela, text="Qual o medicamento que irá utilizar?")
lnome.grid(column=0, row=1)
tfnome = Entry(janela, width=50)
tfnome.grid(column=0, row=2)
ltipo = Label(janela, text="Qual o tipo de remedio?")
ltipo.grid(column=0, row=3)
tftipo = Entry(janela, width=50)
tftipo.grid(column=0, row=4)
ldias = Label(janela, text="Por quantos dias deverá tomar?")
ldias.grid(column=0, row=5)
tfdias = Entry(janela, width=50)
tfdias.grid(column=0, row=6)
ltempo = Label(janela, text="De quantas em quantas horas deverá tomar?")
ltempo.grid(column=0, row=7)
tftempo = Entry(janela, width=50)
tftempo.grid(column=0, row=8)
les = Label(janela, text="       ")
les.grid(column=1)


def registro():
    nome = tfnome.get()
    tipo = tftipo.get()
    dias = tfdias.get()
    tempo = tftempo.get()
    remedio = Medicamento(nome, tipo, dias, tempo)
    janela1 = Tk()
    janela1.title("Dados do remédio")
    janela1.geometry('550x250')
    lremedio1 = Label(janela1, text=remedio)
    lremedio1.grid(column=0, row=0)
    voltar1 = Button(janela1, text="Voltar", command=janela1.destroy)
    voltar1.grid(column=1, row=0)


def btalarmar():
    nome = tfnome.get()
    tipo = tftipo.get()
    dias = tfdias.get()
    dias = int(dias)
    tempo = tftempo.get()
    tempo = int(tempo)
    remedio = Medicamento(nome, tipo, dias, tempo)
    remedio.alarmar()


registra = Button(janela, text="Mostrar entrada", command=registro)
registra.grid(column=2, row=2)
alarma = Button(janela, text="Registrar Alarme", command=btalarmar)
alarma.grid(column=2, row=4)
saia = Button(janela, text="Sair", command=janela.destroy)
saia.grid(column=2, row=6)
janela.mainloop()
