import time
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class Medicamento:

    def __init__(self, nome, tipo, dias, tempo):
        self.nome = nome
        self.tipo = tipo
        self.dias = dias
        self.tempo = tempo

    def update(self, nome, tipo, dias, tempo):
        self.nome = nome
        self.tipo = tipo
        self.dias = dias
        self.tempo = tempo

    def __repr__(self):
        return f"\nRemedio: {self.nome} - {self.tipo}"

    def alarmar(self):

        dia = self.dias
        horas = self.tempo

        janela2 = Tk()
        janela2.title("Testando entrada no Python")
        janela2.geometry('600x250')
        frm1 = ttk.Frame(janela2, padding=40)
        frm1.pack(side=LEFT)
        frm2 = ttk.Frame(janela2, padding=40)
        frm2.pack(side=LEFT)
        lb1 = Label(frm1, text="De quantas em quantas horas deve tomar? ")
        lb1.grid(column=0, row=0)
        lb2 = Label(frm1, text=horas)
        lb2.grid(column=1, row=0)
        lb3 = Label(frm1, text="Estarei definindo os alarmes até a data final")
        lb3.grid(column=0, row=1)
        temp2 = 0

        while dia > 0:
            temp = StringVar()
            temp.set("1")
            tempsup = 1
            while tempsup <= horas:
                time.sleep(1)
                lb4 = Label(frm2, textvariable=temp)
                lb4.grid(column=0, row=0)
                tempsup = tempsup + 1
                temp.set(tempsup)
            temp2 += tempsup
            messagebox.showinfo("Alarme", "Tomar medicamento.")

            if temp2 >= 24:
                dia -= 1
                temp2 = 0
                lb4 = Label(frm2, text="Dias faltando: ")
                lb4.grid(column=0, row=0)
                lb5 = Label(frm2, text=dia)
                lb5.grid(column=1, row=0)
