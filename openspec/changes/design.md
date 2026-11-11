# Arquitetura e Design Técnico da Solução

## 1. Visão Geral da Arquitetura
A aplicação adota uma arquitetura simples e modular baseada em scripts Python e persistência local via SQLite.
## 2. Modelo de Dados Relacional (SQLite)

### Tabela: `produtos`
Armazena os itens cadastrados e o saldo acumulado atual.
- `id`: INTEGER (Primary Key, Autoincrement)
- `nome`: TEXT (NOT NULL) — Nome do ingrediente/produto
- `categoria`: TEXT — Origem ou tipo (ex: Horta, Laticínios, Secos)
- `quantidade_estoque`: REAL (DEFAULT 0.0) — Saldo em estoque
- `unidade_medida`: TEXT (NOT NULL) — Unidade (ex: kg, g, unidade, litro)

### Tabela: `movimentacoes`
Registra o histórico temporal de auditoria de cada transação.
- `id`: INTEGER (Primary Key, Autoincrement)
- `produto_id`: INTEGER (Foreign Key -> `produtos.id`)
- `tipo`: TEXT (CHECK: 'ENTRADA' ou 'SAIDA')
- `quantidade`: REAL (NOT NULL)
- `data_movimentacao`: DATETIME (DEFAULT CURRENT_TIMESTAMP)
- `observacao`: TEXT — Detalhes (ex: "Colheita da manhã", "Molho de tomate")

## 3. Regras de Negócio e Validações
1. **Entrada de Estoque:** Toda movimentação do tipo `ENTRADA` soma a quantidade ao campo `quantidade_estoque` da tabela `produtos`.
2. **Saída de Estoque:** Toda movimentação do tipo `SAIDA` subtrai a quantidade do campo `quantidade_estoque`.
3. **Consistência de Saldo:** O sistema invalida e rejeita qualquer movimentação de `SAIDA` cujo valor seja superior ao `quantidade_estoque` atual do produto.