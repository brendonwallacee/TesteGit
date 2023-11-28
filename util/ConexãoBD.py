import pyodbc


class Conexao:
    def __init__(self):
        pass

    @staticmethod
    def getConnection():
        try:
            conn_str = (
            "Driver={SQL Server};"
            "Server=DESKTOP-VREALUT\APPREMEDIO;"
            "Database=TesteGit;"
            )
            return pyodbc.connect(conn_str)

        except Exception as e:
            raise Exception(str(e))

    @staticmethod
    def closeConnection(conn, stmt=None, rs=None):
        try:
            if rs:
                rs.close()
            if stmt:
                stmt.close()
            if conn:
                conn.close()
        except Exception as e:
            raise Exception(str(e))
