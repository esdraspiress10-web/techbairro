# TechBairro

A TechBairro é um sistema desktop desenvolvido em Python para o cadastro e gerenciamento de clientes de uma associação de moradores.

**Versão atual:** 3.3.1 · Histórico de mudanças no [CHANGELOG](CHANGELOG.MD)

## Funcionalidades

- Cadastrar clientes com nome, telefone, e-mail e endereço.
- Consultar, alterar e excluir clientes cadastrados.

## Requisitos para execução

| Item | Requisito |
|---|---|
| Sistema operacional | Windows |
| Python | Python 3 instalado |
| Tkinter | Necessário para a interface gráfica |
| Bibliotecas externas | Nenhuma |
| Internet | Necessária apenas para baixar o projeto |

## Instalação

### Opção 1 — Baixar pelo Git

Abra o terminal e execute:

```bash
git clone https://github.com/esdraspiress10-web/techbairro.git
```

Entre na pasta do projeto:

```bash
cd techbairro
```

### Opção 2 — Baixar pelo GitHub

1. Acesse o repositório da TechBairro no GitHub.
2. Clique no botão **Code**.
3. Selecione **Download ZIP**.
4. Extraia o arquivo ZIP.
5. Abra a pasta extraída no VS Code.

### Executar o programa

No terminal, dentro da pasta do projeto, execute:

```bash
python techbairro.py
```

Ao executar, a janela principal da TechBairro será aberta. No terminal, também aparecerá a mensagem indicando o banco de dados em uso.

### Dependências

O projeto utiliza apenas bibliotecas da própria instalação do Python. O arquivo [requirements.txt](requirements.txt) registra essa informação.

## Configuração do banco de dados

A TechBairro utiliza o SQLite para armazenar os dados dos clientes.

O banco de dados é criado automaticamente quando o programa é iniciado, caso ainda não exista.

O arquivo utilizado é o `techbairro.db`. Ele fica na pasta do projeto e armazena os clientes cadastrados.

O banco de dados não deve ser enviado ao GitHub, pois pode conter dados pessoais dos clientes.

Para fazer uma cópia de segurança, feche o programa e copie o arquivo `techbairro.db` para uma pasta segura.

## Como usar

O passo a passo está no [Manual de uso](docs/manual_de_uso.md).

## Estrutura do projeto

| Arquivo ou pasta | Descrição |
|---|---|
| `techbairro.py` | Arquivo principal do sistema |
| `banco.py` | Gerenciamento do banco de dados |
| `cliente.py` | Modelo de cliente |
| `validacao.py` | Regras de validação dos dados |
| `testar_validacao.py` | Testes das validações |
| `scripts/` | Scripts auxiliares do projeto |
| `docs/` | Documentação de uso |
| `CHANGELOG.MD` | Histórico de mudanças |
| `requirements.txt` | Registro das dependências |
| `.gitignore` | Arquivos que não devem ser enviados ao GitHub |

## Autor

Esdras Soares Pires

Técnico em Desenvolvimento de Sistemas — Senac DF

