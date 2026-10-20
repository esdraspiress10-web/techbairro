
import tkinter as tk
from tkinter import messagebox
from cliente import Cliente
from banco import GerenciadorClientes
from validacao import ValidadorCliente

CAMINHO_BANCO = "techbairro.db"
VERSAO = "3.3.1"

gerenciador = GerenciadorClientes(CAMINHO_BANCO)
validador = ValidadorCliente()

janela = tk.Tk()
janela.title("TechBairro")
janela.geometry("480x460")

tk.Label(janela, text="TechBairro", font=("Arial", 18)).pack(pady=10)

campos = {}
for nome in ["Nome", "Telefone", "E-mail", "Endereço"]:
    tk.Label(janela, text=nome).pack()
    entrada = tk.Entry(janela, width=40)
    entrada.pack()
    campos[nome] = entrada

status = tk.Label(janela, text="")
status.pack(pady=5)


def salvar():
    valores = {nome: entrada.get() for nome, entrada in campos.items()}

    cliente = Cliente(
        valores["Nome"],
        valores["Telefone"],
        valores["E-mail"],
        valores["Endereço"]
    )

    erro = validador.validar(cliente)
    if erro is not None:
        status.config(text=erro, fg="red")
        return

    try:
        gerenciador.conexao.execute(
            "INSERT INTO clientes (nome, telefone, email, endereco) VALUES (?, ?, ?, ?)",
            (cliente.nome, cliente.telefone, cliente.email, cliente.endereco)
        )
        gerenciador.conexao.commit()
        status.config(text="Cliente cadastrado com sucesso!", fg="green")

        for entrada in campos.values():
            entrada.delete(0, tk.END)

    except Exception as erro:
        messagebox.showerror("Erro", str(erro))
      

def consultar():
    consulta = tk.Toplevel(janela)
    consulta.title("Consulta de clientes")

    lista = tk.Listbox(consulta, width=60)
    lista.pack(padx=10, pady=10)

    registros = gerenciador.conexao.execute(
        "SELECT id, nome, telefone, email, endereco FROM clientes ORDER BY nome"
    ).fetchall()

    for registro in registros:
        lista.insert(tk.END, f"{registro[0]} - {registro[1]} - {registro[2]}")


def fechar():
    gerenciador.fechar()
    janela.destroy()


tk.Button(janela, text="Salvar cliente", command=salvar).pack(pady=5)
tk.Button(janela, text="Consultar clientes", command=consultar).pack(pady=5)

janela.protocol("WM_DELETE_WINDOW", fechar)
janela.mainloop()
