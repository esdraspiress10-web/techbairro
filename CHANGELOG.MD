# Changelog

## Em desenvolvimento
### Adicionado
- Código publicado no GitHub, com histórico de versões.

## v3.3.1 (Aula 21)
### Alterado
- O código do sistema foi refatorado e separado em camadas (Modelo, Dados, Regras de Negócio e Tela).
- As regras de validação do cadastro saíram do arquivo principal e foram isoladas na classe `ValidadorCliente`.

### Adicionado
- Módulo `cliente.py` para representar os dados de um cliente.
- Módulo `banco.py` para gerenciar toda a comunicação com o banco SQLite.
- Módulo `validacao.py` contendo as regras de negócio de cadastro.
- Script de testes automatizados `testar_validacao.py` para conferir as regras de negócio sem abrir a janela.

## v3.3.0 (Aula 20)
### Alterado
- Melhorada a segurança nas operações de alteração e exclusão de registros utilizando a seleção direta da tela.
- O modo de edição passou a contar com validações e feedback visual mais claros.

## v3.2.1 (Aula 18)
### Alterado
- O número da versão passou a ser centralizado em uma única constante no código.

### Adicionado
- Script `scripts/gerar_pacote.py` para automatizar a criação do arquivo `.zip` de distribuição.
- Arquivo `COMO_EXECUTAR.txt` com instruções para a execução do programa.