import sqlite3


class GerenciadorClientes:
    def __init__(self, caminho_banco):
        self.conexao = sqlite3.connect(caminho_banco)
        self.criar_tabela()

    def criar_tabela(self):
        self.conexao.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT NOT NULL,
                email TEXT NOT NULL,
                endereco TEXT NOT NULL
            )
        """)
        self.conexao.commit()

    def excluir_cliente(self, cliente_id):
        self.conexao.execute(
            "DELETE FROM clientes WHERE id = ?",
            (cliente_id,)
        )
        self.conexao.commit()

    def fechar(self):
        self.conexao.close() 