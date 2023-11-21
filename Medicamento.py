import time


class Medicamento:

    def __init__(self, nome, tipo, dias, tempo):
        self.nome = nome
        self.tipo = tipo
        self.dias = dias
        self.tempo = tempo

    def __repr__(self):
        return f"\nRemedio: {self.nome} - {self.tipo}"

    def alarmar(self):
        print("\nVocê deve tomar a cada", self.tempo, " horas\nEstarei definindo os alarmes até a data final\n")
        temp2 = 0

        while self.dias > 0:
            temp = 1

            while temp <= self.tempo:
                time.sleep(1)
                print(temp)
                temp = temp + 1
            temp2 += temp

            print("Tomar ", self.nome)

            if temp2 >= 24:
                self.dias -= 1
                temp2 = 0
                print("dias faltando = ", self.dias)
