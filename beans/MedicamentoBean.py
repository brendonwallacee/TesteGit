class MedicamentoBean:

    def MedicamentoBean(self, nome, dias, tempo):
        self._nome = nome
        self._dias = dias
        self._tempo = tempo

    def __init__(self, nome, tipo, dias, tempo):
        self._nome = nome
        self._tipo = tipo
        self._dias = dias
        self._tempo = tempo

    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome

    def getTipo(self):
        return self._tipo

    def setTipo(self, tipo):
        self._tipo = tipo

    def getDias(self):
        return self._dias

    def setDias(self, dias):
        self._dias = dias

    def getTempo(self):
        return self._tempo

    def setTempo(self, tempo):
        self._tempo = tempo
