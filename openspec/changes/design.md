# Design do Sistema de Estoque

## 1. Arquitetura da Solução
O sistema utilizará Python no backend e SQLite como banco de dados relacional.

## 2. Estrutura do Banco de Dados

### Tabela: `produtos`
- `id` (INTEGER, Primary Key, Autoincrement)
- `nome` (TEXT, NOT NULL)
- `categoria` (TEXT)
- `quantidade_estoque` (REAL, DEFAULT 0.0)
- `unidade_medida` (TEXT, NOT NULL)

### Tabela: `movimentacoes`
- `id` (INTEGER, Primary Key, Autoincrement)
- `produto_id` (INTEGER, Foreign Key -> `produtos.id`)
- `tipo` (TEXT, CHECK: 'ENTRADA' ou 'SAIDA')
- `quantidade` (REAL, NOT NULL)
- `data_movimentacao` (DATETIME, DEFAULT CURRENT_TIMESTAMP)
- `observacao` (TEXT)

## 3. Regras de Negócio
- Registrar uma movimentação do tipo `ENTRADA` soma o valor ao `quantidade_estoque`.
- Registrar uma movimentação do tipo `SAIDA` subtrai o valor do `quantidade_estoque`.
- Não é permitido registrar uma `SAIDA` maior do que o saldo disponível em estoque.