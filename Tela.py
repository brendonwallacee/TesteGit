from tkinter import *
from tkinter import ttk
from Medicamento import Medicamento

janela = Tk()
janela.title("Testando entrada no Python")
janela.geometry('600x250')
frm1 = ttk.Frame(janela, padding=40)
frm1.pack(side=LEFT)
frm2 = ttk.Frame(janela, padding=40)
frm2.pack(side=LEFT)

lnome = Label(frm1, text="Qual o medicamento que irá utilizar?")
lnome.grid(column=0, row=1)
tfnome = Entry(frm1, width=50)
tfnome.grid(column=0, row=2)
ltipo = Label(frm1, text="Qual o tipo de remedio?")
ltipo.grid(column=0, row=3)
tftipo = Entry(frm1, width=50)
tftipo.grid(column=0, row=4)
ldias = Label(frm1, text="Por quantos dias deverá tomar?")
ldias.grid(column=0, row=5)
tfdias = Entry(frm1, width=50)
tfdias.grid(column=0, row=6)
ltempo = Label(frm1, text="De quantas em quantas horas deverá tomar?")
ltempo.grid(column=0, row=7)
tftempo = Entry(frm1, width=50)
tftempo.grid(column=0, row=8)


def registro():
    nome = str(tfnome.get())
    tipo = str(tftipo.get())
    dias = int(tfdias.get())
    tempo = int(tftempo.get())
    remedio = Medicamento(nome, tipo, dias, tempo)


def entrada():
    janela1 = Tk()
    janela1.title("Dados do remédio")
    janela1.geometry('550x50')

    nome = str(tfnome.get())
    tipo = str(tftipo.get())
    dias = int(tfdias.get())
    tempo = int(tftempo.get())
    remedio = Medicamento(nome, tipo, dias, tempo)

    lremedio1 = Label(janela1, text=str(remedio))
    lremedio1.pack(side=LEFT, padx=20)
    voltar1 = Button(janela1, text="Voltar", command=janela1.destroy)
    voltar1.pack(side=RIGHT, padx=20)


def alarme():
    nome = str(tfnome.get())
    tipo = str(tftipo.get())
    dias = int(tfdias.get())
    tempo = int(tftempo.get())
    remedio = Medicamento(nome, tipo, dias, tempo)
    remedio.alarmar()


btreg = Button(frm2, text="Salvar", command=registro, width=20, height=2, borderwidth=2)
btreg.grid(column=0, row=1, padx=10, pady=5)

btalarm = Button(frm2, text="Registrar Alarme", command=alarme, width=20, height=2)
btalarm.grid(column=0, row=2, padx=10, pady=5)

saia = Button(frm2, text="Sair", command=janela.destroy, width=20, height=2)
saia.grid(column=0, row=3, padx=10, pady=5)

mostra = Button(frm2, text="Mostrar Entrada", command=entrada, width=20, height=2, borderwidth=2)
mostra.grid(column=0, row=4, padx=10, pady=5)

janela.mainloop()
