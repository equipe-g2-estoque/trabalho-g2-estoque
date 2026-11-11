# Plano de Tarefas e Status de Implementação

## Fase 1: Arquitetura & Banco de Dados
- [x] Modelar o esquema relacional entre `produtos` e `movimentacoes`.
- [x] Criar o script `database.py` e inicializar o banco de dados `estoque.db`.
- [x] Garantir a criação das chaves primárias e estrangeiras.

## Fase 2: Implementação do Backend & Operações CRUD
- [x] Criar a interface de menu interativo no arquivo `main.py`.
- [x] Implementar a função de inclusão de novos produtos (Create).
- [x] Implementar a consulta e listagem de produtos com saldo (Read).
- [x] Implementar a movimentação de entrada/saída com atualização de saldo (Update).
- [x] Implementar a validação de quantidade mínima para evitar saldo negativo.
- [x] Implementar a remoção de produtos cadastrados (Delete).

## Fase 3: Versionamento, Organização & Documentação
- [x] Estruturar os artefatos da metodologia OpenSpec (`proposal.md`, `design.md`, `tasks.md`).
- [x] Criar e configurar o archivo `.gitignore` para o ambiente Python/SQLite.
- [x] Migrar o repositório para a Organização GitHub `equipe-g2-estoque`.
- [x] Concluir o versionamento e sincronização do ramo `main`.