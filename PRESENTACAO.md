# Roteiro de Apresentação — Sistema de Gestão de Estoque (G2)

## Integrantes do Grupo
- Sante Biondi
- Arthur Radtke Machado
- Gustavo Ellwanger

---

## Estrutura da Apresentação (Divisão de Fala)

### 1. Introdução & Demonstração Prática (Sante Biondi)
- **Problema Real:** Controle de fluxo entre a produção agrícola da horta e o consumo no restaurante.
- **Demonstração:** Execução do programa via CLI (`uv run main.py`).
- **Operações CRUD:** Apresentação do cadastro de produtos, listagem em tempo real, registro de entradas/saídas e validação de saldo para evitar giros negativos.

### 2. Arquitetura do Banco de Dados (Arthur Radtke Machado)
- **Modelagem Relacional:** Estrutura das tabelas no SQLite (`estoque.db`).
- **Tabelas:** Relacionamento entre a tabela `produtos` (cadastro e saldo) e a tabela `movimentacoes` (histórico de auditoria com carimbo de data/hora).
- **Integridade:** Utilização de Chave Estrangeira (`produto_id`) e restrições de validação.

### 3. Metodologia OpenSpec & Organização no GitHub (Gustavo Ellwanger)
- **Framework OpenSpec:** Explicação das 4 fases (Explore, Propose, Apply, Verify) e exibição dos artefatos em `openspec/changes/` (`proposal.md`, `design.md`, `tasks.md`).
- **Trabalho em Equipe:** Organização `equipe-g2-estoque` no GitHub e fluxo de versionamento conjunto na branch `main`.