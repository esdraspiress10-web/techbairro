# Registro de testes da TechBairro

**Versão testada:** 3.3.2  
**Data:** 26/10/2026  
**Responsável:** Esdras  
**Sistema operacional:** Windows  
**Versão do Python:** preencher com a versão instalada

## Testes manuais

| ID | Requisito | Passos e dados | Esperado | Obtido | Status |
|---|---|---|---|---|---|
| CT01 | RF01 | Cadastrar um cliente com todos os campos corretos | Cliente cadastrado com sucesso | Preencher após executar | Pendente |
| CT02 | RF01 | Salvar com Nome e Endereço vazios | Sistema impede o cadastro e informa o erro | Preencher após executar | Pendente |
| CT03 | RF02 | Informar telefone `61 9999 0000` com espaços | Sistema valida o telefone conforme as regras do projeto | Preencher após executar | Pendente |
| CT04 | RF03 | Informar e-mail `ana@email`, sem ponto | Sistema rejeita o e-mail inválido | Preencher após executar | Pendente |
| CT05 | RF05 | Editar um cliente, trocar o telefone e salvar | Telefone atualizado corretamente | Preencher após executar | Pendente |
| CT06 | RF06 | Tentar excluir um cliente, responder Não e depois Sim | Primeiro mantém o cliente; depois confirma a exclusão | Preencher após executar | Pendente |

## Testes automáticos

**Comando:** `python testar_validacao.py`

**Resultado:** preencher após executar o comando.

## Defeitos encontrados

Preencher após executar os testes, informando o que falhou e como foi corrigido, ou escrever "nenhum" se nenhum defeito for encontrado.
