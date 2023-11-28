import time
from persistencia.MedicamentoDAOListener import *
from beans.MedicamentoBean import *
from util.ConexãoBD import *


class MedicamentoDAO(MedicamentoDAOListener):
    conn = None

    def __init__(self):
        try:
            Conexao.getConnection()
        except Exception as e:
            raise Exception("Erro: " + str(e))

    def salvar(self, remedio: MedicamentoBean) -> None:
        cursor = None
        if remedio is None:
            raise Exception("O valor passado não pode ser nulo")

        try:
            SQL = "INSERT INTO Medicamento(nome, tipo, dias, tempo) values (?, ?, ?, ?)"
            cursor = self.conn.cursor()
            cursor.execute(SQL, remedio.getNome(), remedio.getTipo(), remedio.getDias(), remedio.getTempo())
            self.conn.commit()
        except pyodbc.Error as e:
            raise Exception("Erro ao inserir dados" + str(e))
        finally:
            a = "Salvo com Sucesso"
            Conexao.closeConnection(cursor)
            print(a)

    def excluir(self, remedio: MedicamentoBean) -> None:
        cursor = None
        if remedio is None:
            raise Exception("O valor passado não pode ser nulo")

        try:
            SQL = "DELETE From Medicamento where nome=?"
            cursor = self.conn.cursor()
            cursor.execute(SQL, remedio.getNome())
            self.conn.commit()
        except pyodbc.Error as e:
            raise Exception("Erro ao inserir dados" + str(e))
        finally:
            Conexao.closeConnection(cursor)

    def atualizar(self, remedio: MedicamentoBean) -> None:
        cursor = None
        if remedio is None:
            raise Exception("O valor passado não pode ser nulo")

        try:
            SQL = "UPDATE Medicamento SET nome = ?, tipo = ?, dias = ?, tempo = ?"
            cursor = self.conn.cursor()
            cursor.execute(SQL, remedio.getNome(), remedio.getTipo(), remedio.getDias(), remedio.getTempo())
            self.conn.commit()

        except pyodbc.Error as e:
            raise Exception("Erro ao inserir dados" + str(e))
        finally:
            Conexao.closeConnection(cursor)

    def todosMedicamentos(self) -> List:
        Conexao.getConnection()
        cursor = self.conn.cursor()

        SQL = "SELECT * From Medicamento"
        cursor.execute(SQL)

        list = []
        for row in cursor.fetchall():
            nome = row[0]
            dias = row[2]
            tempo = row[3]
            remedio = MedicamentoBean(nome, dias, tempo)
            list.append(remedio)

        Conexao.closeConnection(cursor)
        return list

    def procurarMedicamento(self, nome: str) -> MedicamentoBean:
        Conexao.getConnection()
        cursor = self.conn.cursor()

        try:
            SQL = "SELECT * From Medicamento Where Nome = ?"
            cursor.execute(SQL, nome)
            row = cursor.fetchone()

            if not row:
                raise Exception("Nenhum registro encontrado com o nome: " + str(nome))

            nome = row[0]
            dias = row[2]
            tempo = row[3]

            return MedicamentoBean(nome, dias, tempo)

        except pyodbc.Error as e:
            raise Exception(e)

        finally:
            Conexao.closeConnection(cursor)

    def alarmar(self, remedio: MedicamentoBean, hora) -> None:
        dias = remedio.getDias()
        tempo = remedio.getTempo()
        tempTotal = dias * 24
        qtRemedio = int(tempTotal / tempo)


        cont = 1

        list = []
        while cont <= qtRemedio:
            list.append(hora)
            hora += tempo
            if hora > 24:
                hora = self.hora

            cont = cont + 1

        print(list)
